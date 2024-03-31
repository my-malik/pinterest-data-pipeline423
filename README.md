# Pinterest Data Pipeline

## Introduction

The Pinterest Data Pipeline project integrates batch and stream processing workflows for Pinterest data and runs it through a pipeline. The three main tables used from the AWS RDS were:
- Pinterest Data
- Geolocation Data
- User Data

The following Technologies were used:
- EC2 Kafka Client
- MSK Cluster
- S3 Bucket
- API Integration
- AWS Kinesis
- Airflow
- Databricks

## Table of Contents

- [Milestone 2](#milestone-2)
- [Milestone 3](#milestone-3)
- [Milestone 4](#milestone-4)
- [Milestone 5](#milestone-5)
- [Milestone 6](#milestone-6)
- [Milestone 7](#milestone-7)
- [Milestone 8](#milestone-8)
- [Milestone 9](#milestone-9)
- [Usage](#usage)
- [Features](#features)



## Milestone 2

The user_posting_emulation.py was used to print out data from the three tables containing Pinterest, Geolocation and User data by connecting to AWS RDS Database

## Milestone 3

An EC2 Kafka Client was setup by installing Kafka on the EC2 instance. Thereafter, 3 Kafka topics were created for Pinterest, Geolocation and User data respectively

## Milestone 4
A custom plugin with MSK Connect was created by downloading Confluent.io Amazon S3 Connector, which was copied to an S3 Bucket. A connector was setup after creating the plugin, allowing data from the Kafka topics to be stored in the S3 Bucket

## Milestone 5
An API will allow data to be sent to the MSK Cluster, which will be stored in the S3 Bucket using the connector created. A Kafka REST Proxy was setup on the EC2 instance and thereafter data was sent from eahc of the table to their corresponding Kakfa topics using the API from the user_posting_emulation.py

## Milestone 6
The S3 Bucket previously used was mounted to Databricks in order to read the data from the data stored in the S3 Bucket. 3 Dataframes were created to read in the data from each of tables.

## Milestone 7
The data from the S3 Bucket was processed in Databricks by cleaning the data from each of the 3 Dataframes created. After cleaning the data, various queries were run using Spark to retrieve relevant insights.

## Milestone 8
MWAA was used to run Batch Processing on Databricks. An Airflow DAG was created in order to trigger the Databricks Notebook, which was run daily.

## Milestone 9
Kinesis was used for Stream Processing. 3 data streams were setup, one for each table.
An API was configured to allow Kinesis actions with the capabilities of the following: Creating, Describing, Deleting, Listing and adding recording to streams in Kinesis.

The following script user_posting_emulation_streaming.py was used to send requests to the API, which added one record at a time to the streams from each of the three tables to their corresponding Kinesis Stream.


A Notebook in Databricks was used to read in the data from the Kinesis Streams, with cleaning operations performed as they were processed. The cleaned data was then written to a Delta Table for each of the streams.


