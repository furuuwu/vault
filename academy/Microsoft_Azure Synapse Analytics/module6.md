# module 6

* Build a data pipeline in Azure Synapse Analytics
  * Understand pipelines in Azure Synapse Analytics
  * Create a pipeline in Azure Synapse Studio
  * Define data flows
  * Run a pipeline
  * [lab](https://microsoftlearning.github.io/dp-203-azure-data-engineer/Instructions/Labs/10-Synpase-pipeline.html)

## pipelines in Azure Synapse Analytics

Pipelines in Azure Synapse Analytics encapsulate a sequence of activities that perform data movement and processing tasks. You can use a pipeline to define data transfer and transformation activities, and orchestrate these activities through control flow activities that manage branching, looping, and other typical processing logic. The graphical design tools in Azure Synapse Studio enable you to build complex pipelines with minimal or no coding required.

Azure Synapse Analytics pipelines are built on the same technology as Azure Data Factory, and offer a similar authoring experience. The authoring processes described in this module are also applicable to Azure Data Factory.

![a](img/2025-01-17-12-30-34.png)

* activities

  Activities are the executable tasks in a pipeline. You can define a flow of activities by connecting them in a sequence. The outcome of a particular activity (success, failure, or completion) can be used to direct the flow to the next activity in the sequence.

  Activities can encapsulate data transfer operations, including simple data copy operations that extract data from a source and load it to a target (or sink), as well as more complex data flows that apply transformations to the data as part of an extract, transfer, and load (ETL) operation. Additionally, there are activities that encapsulate processing tasks on specific systems, such as running a Spark notebook or calling an Azure function. Finally, there are control flow activities that you can use to implement loops, conditional branching, or manage variable and parameter values.

* integration runtime

  The pipeline requires compute resources and an execution context in which to run. The pipeline's integration runtime provides this context, and is used to initiate and coordinate the activities in the pipeline.

* linked services

  While many of the activities are run directly in the integration runtime for the pipeline, some activities depend on external services. For example, a pipeline might include an activity to run a notebook in Azure Databricks or to call a stored procedure in Azure SQL Database. To enable secure connections to the external services used by your pipelines, you must define linked services for them.

* datasets

  Most pipelines process data, and the specific data that is consumed and produced by activities in a pipeline is defined using datasets. A dataset defines the schema for each data object that will be used in the pipeline, and has an associated linked service to connect to its source. Activities can have datasets as inputs or outputs.

## Create a pipeline

When you create a pipeline in Azure Synapse Studio, you can use the graphical design interface.

![a](img/2025-01-17-12-33-36.png)

The pipeline designer includes a set of activities, organized into categories, which you can drag onto a visual design canvas. You can select each activity on the canvas and use the properties pane beneath the canvas to configure the settings for that activity.

To define the logical sequence of activities, you can connect them by using the Succeeded, Failed, and Completed dependency conditions, which are shown as small icons on the right-hand edge of each activity.

While the graphical development environment is the preferred way to create a pipeline, you can also create or edit the underlying JSON definition of a pipeline. The following code example shows the JSON definition of a pipeline that includes a Copy Data activity:

```json
{
  "name": "CopyPipeline",
  "properties": {
    "description": "Copy data from a blob to Azure SQL table",
    "activities": [
      {
        "name": "CopyFromBlobToSQL",
        "type": "Copy",
        "inputs": [
          {
            "name": "InputDataset"
          }
        ],
        "outputs": [
          {
            "name": "OutputDataset"
          }
        ],
        "typeProperties": {
          "source": {
            "type": "BlobSource"
          },
          "sink": {
            "type": "SqlSink",
            "writeBatchSize": 10000,
            "writeBatchTimeout": "60:00:00"
          }
        },
        "policy": {
          "retry": 2,
          "timeout": "01:00:00"
        }
      }
    ]
  }
}
```

A Data Flow is a commonly used activity type to define data flow and transformation. Data flows consist of:

* Sources - The input data to be transferred.
* Transformations – Various operations that you can apply to data as it streams through the data flow.
* Sinks – Targets into which the data will be loaded.

When you add a Data Flow activity to a pipeline, you can open it in a separate graphical design interface in which to create and configure the required data flow elements.

![a](img/2025-01-17-12-35-45.png)

An important part of creating a data flow is to define mappings for the columns as the data flows through the various stages, ensuring column names and data types are defined appropriately. While developing a data flow, you can enable the Data flow debug option to pass a subset of data through the flow, which can be useful to test that your columns are mapped correctly.

<https://learn.microsoft.com/en-us/azure/data-factory/control-flow-execute-data-flow-activity>

## Run a pipeline

When you’re ready, you can publish a pipeline and use a trigger to run it. Triggers can be defined to run the pipeline:

* Immediately
* At explicitly scheduled intervals
* In response to an event, such as new data files being added to a folder in a data lake.

You can monitor each individual run of a pipeline in the Monitor page in Azure Synapse Studio.

![a](img/2025-01-17-12-37-07.png)

The ability to monitor past and ongoing pipeline runs is useful for troubleshooting purposes. Additionally, when combined with the ability to integrate Azure Synapse Analytics and Microsoft Purview, you can use pipeline run history to track data lineage data flows.

<https://learn.microsoft.com/en-us/training/modules/intro-to-microsoft-purview/>
