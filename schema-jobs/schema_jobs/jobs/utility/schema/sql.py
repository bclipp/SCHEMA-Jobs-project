def deploy_sql(sql:str):
    spark.sql(sql)