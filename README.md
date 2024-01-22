[![Format](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project3/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project3/actions/workflows/format.yml)
[![Install](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project3/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project3/actions/workflows/install.yml)
[![Test](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project3/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project3/actions/workflows/test.yml)
[![Lint](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project3/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project3/actions/workflows/Lint.yml)



IDS706_DataEngineering_BarbaraFlores_Project3
# 📂  Databricks ETL Pipeline

The main goal of this project is to develop a meticulously documented Databricks notebook that performs ETL operations, ensuring effective use of Delta Lake for data storage, and employing Spark SQL for the necessary transformations.

### 🎥 Video Tutorial
The following [YouTube link](https://youtu.be/EFe9FRIGIUc) shows a clear, concise walkthrough and demonstration of the project


### 📊 Database

For this project, we will utilize the [Top Spotify Songs in 73 Countries](https://www.kaggle.com/datasets/asaniczka/top-spotify-songs-in-73-countries-daily-updated/) dataset. This dataset provides a comprehensive view of the top songs trending in over 70 countries, offering valuable insights into the dynamics of the music industry. It includes a wide range of information on the most popular songs in the world, such as unique Spotify identifiers, song names, artists, daily rankings, daily movement in rankings, and more.

This dataset comprises 25 variables (columns) and was extracted on 2023-11-05. In total, it contains 72.959 records.

### 🚀 Delta Lake

Our ETL pipeline stands on the robust foundation of Delta Lake as the chosen data storage system. This decision is pivotal for ensuring the reliability and efficiency of our data processing workflow. Delta Lake's support for atomic transactions plays a key role in maintaining data consistency during write operations, while its ability to handle incremental writes and version data simplifies tracking and recovery, a crucial aspect for effective data management. The optimized performance for both read and write operations further strengthens our pipeline's capability to handle substantial data volumes efficiently.

Demonstrating a keen understanding of Delta Lake's distinctive features, including time travel and metadata management, we acknowledge the significance of managing data evolution over time. This not only enhances our data storage strategy but also positions our ETL pipeline to adapt seamlessly to evolving data requirements. Additionally, our commitment to data quality is evident through the integration of data validation checks within the notebook. These checks act as a vital safeguard, ensuring the processed data maintains high standards of reliability and integrity. The strategic use of Delta Lake underscores our dedication to delivering a resilient, high-quality, and future-ready ETL solution.


### 🔄 Databricks ETL Pipeline

In this project, Extract, Transform, and Load (ETL) operations were carried out using the following approach:

**Extract:**
In the [Extract.py](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project3/blob/main/src/Extract.py) file, data extraction was performed from the original source, a CSV file named `UniversalTopSpotifySongs.csv`. The data was read and converted to a Spark DataFrame, and then stored in a Delta table named `RawUniversalTopSpotifySongs` for further processing.

**Transform:**
Data transformation took place in the [TransformLoad.py](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project3/blob/main/src/TransformLoad.py) file. Using Spark SQL, transformations were applied, including converting certain fields to uppercase and modifying date formats. These transformations were applied to the `RawUniversalTopSpotifySongs` DataFrame, and the results were stored in a new Delta table named `CleanUniversalTopSpotifySongs`.

**Load:**
The loading operation was also performed in the [TransformLoad.py](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project3/blob/main/src/TransformLoad.py) file. The transformed data was written to a Delta table, specifically to the file `/FileStore/tables/CleanUniversalTopSpotifySongs.delta`. This process ensures that the transformed data is efficiently and structurally available for further analysis.


### 📈 Spark SQL Implementation

Spark SQL plays a pivotal role in our ETL pipeline, driving effective data transformations across all stages. It is strategically implemented in [Extract.py](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project3/blob/main/src/Extract.py)  to read and convert data into a Spark DataFrame, in [TransformLoad.py](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project3/blob/main/src/TransformLoad.py) to apply transformations on the RawUniversalTopSpotifySongs DataFrame, and in [Analize.py](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project3/blob/main/src/Analize.py)  to perform advanced analytics on the CleanUniversalTopSpotifySongs Delta table. This consistent use of Spark SQL underscores our commitment to leveraging advanced technologies for efficient and effective data processing throughout the entire pipeline.

### 🧐 Visualization and Conclusion
In the file [Analize.py](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project3/blob/main/src/Analize.py), we can observe the analysis of our data. On a global scale and during the evaluation period (from October 18, 2023, to November 5, 2023), the most listened-to artists on Spotify, within the top 50 of various countries, included:

- "TAYLOR SWIFT"
- "BAD BUNNY"
- "DOJA CAT"
- "BIZARRAP"
- "MILO J"
- "TATE MCRAE"
- "IÑIGO QUINTERO"

![15.png](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project3/main/images/15.png)  

Subsequently, we can visualize how the average position of each artist behaved in the rankings across different countries in the following graph.

![16.png](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project3/main/images/16.png)  


The analysis of the dataset spanning from October 18, 2023, to November 5, 2023, reveals a global music landscape dominated by artists such as "TAYLOR SWIFT," "BAD BUNNY," "DOJA CAT," and others, consistently featured in the top 50 charts of various countries. This suggests not only their widespread appeal but also the existence of diverse musical preferences globally, spanning genres from pop to Latin and urban. The international presence of artists like "BAD BUNNY" and "DOJA CAT" underscores the influence of cross-cultural collaborations on global popularity. Examining the artists' average rankings over time may uncover periodic trends, shedding light on the dynamic nature of music preferences. In essence, this analysis provides a snapshot of the music industry during the specified period, offering insights into both the consistent popularity of certain artists and the ever-evolving global musical landscape.

### ⏰ Automated Trigger

Finally, the three notebooks in this project have been automated within a Databricks workflow, as showcased in the screencasts and detailed in the demo video. The automated trigger has been meticulously set up to seamlessly initiate the pipeline based on a predefined schedule or event, ensuring the efficiency and reliability of the entire data engineering and analysis process.

### 📸 Workflow Snapshot
In the upcoming section, we provide a visual walkthrough of our data engineering and analysis process. Through a series of screenshots, you'll be guided step by step, gaining insights into the intricacies of our workflow. These snapshots offer a comprehensive view of the tools, methods, and key stages that contribute to our data analysis journey. Let's dive into the details and explore the inner workings of our process

![01.png](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project3/main/images/01.png)

![02.png](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project3/main/images/02.png)

![03.png](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project3/main/images/03.png)

![04.png](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project3/main/images/04.png)

![05.png](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project3/main/images/05.png)

![06.png](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project3/main/images/06.png)

![07.png](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project3/main/images/07.png)

![08.png](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project3/main/images/08.png)

![09.png](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project3/main/images/09.png)

![10.png](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project3/main/images/10.png)

![11.png](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project3/main/images/11.png)

![12.png](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project3/main/images/12.png)

![125.png](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project3/main/images/125.png)

![13.png](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project3/main/images/13.png)

![14.png](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project3/main/images/14.png)


