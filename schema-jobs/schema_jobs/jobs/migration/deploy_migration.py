from schema_jobs.jobs.utility.schema.migration import migrations


def deploy_migration():
    ""
    for migration in migrations:
        deploy_migration(migration())


if __name__ == "__main__":
    deploy_migration()
