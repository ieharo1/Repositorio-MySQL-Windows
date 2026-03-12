import os

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as sum_, avg, desc

MYSQL_HOST = os.getenv("MYSQL_HOST", "mysql")
MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")
MYSQL_USER = os.getenv("MYSQL_USER", "sales")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "salespass")
MYSQL_DB = os.getenv("MYSQL_DB", "salesdb")


def main():
    spark = (
        SparkSession.builder.appName("SalesAnalytics")
        .config(
            "spark.jars",
            "/opt/spark/jars/mysql-connector-j.jar",
        )
        .getOrCreate()
    )

    jdbc_url = f"jdbc:mysql://{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
    props = {
        "user": MYSQL_USER,
        "password": MYSQL_PASSWORD,
        "driver": "com.mysql.cj.jdbc.Driver",
    }

    df = spark.read.jdbc(jdbc_url, "sales", properties=props)

    total_sales = df.select((col("quantity") * col("price")).alias("amount")).groupBy().agg(
        sum_("amount").alias("ventas_totales")
    )

    top_products = (
        df.groupBy("product")
        .agg(sum_("quantity").alias("unidades"))
        .orderBy(desc("unidades"))
        .limit(5)
    )

    sales_by_region = (
        df.select((col("quantity") * col("price")).alias("amount"), col("region"))
        .groupBy("region")
        .agg(sum_("amount").alias("ventas_region"))
        .orderBy(desc("ventas_region"))
    )

    avg_by_customer = (
        df.select((col("quantity") * col("price")).alias("amount"), col("customer_id"))
        .groupBy("customer_id")
        .agg(avg("amount").alias("promedio_cliente"))
        .orderBy(desc("promedio_cliente"))
        .limit(10)
    )

    print("=== Ventas Totales ===")
    total_sales.show(truncate=False)
    print("=== Top Productos ===")
    top_products.show(truncate=False)
    print("=== Ventas por Region ===")
    sales_by_region.show(truncate=False)
    print("=== Promedio por Cliente ===")
    avg_by_customer.show(truncate=False)

    spark.stop()


if __name__ == "__main__":
    main()

