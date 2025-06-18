from py4j.java_gateway import JavaGateway


def process():
    gateway = JavaGateway()
    echo = gateway.jvm.Echo()
    result = echo.print("sigma")

if __name__ == "__main__":
    process()