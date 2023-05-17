from schema_jobs.jobs.configuration.database_configuration import DatabaseConfig


def deploy_database(config: DatabaseConfig):
    spark.sql(f"CREATE DATABASE IF NOT EXISTS {DatabaseConfig.database_name};")
