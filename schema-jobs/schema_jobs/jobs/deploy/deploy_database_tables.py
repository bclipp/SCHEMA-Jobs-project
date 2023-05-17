from schema_jobs.jobs.utility.schema.database import deploy_database
from schema_jobs.jobs.utility.schema.table import deploy_table
from schema_jobs.jobs.configuration.table_configs import tables

def deploy_database_tables():
    ""
    deploy_database()
    for table in tables:
        deploy_table(table)


if __name__ == "__main__":
    deploy_database_tables()