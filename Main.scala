import py4j.GatewayServer

class Echo {
    def print(input: String) {
        prinln(input)
    }
}

object Main {
    def main(args: Array[String]) = {
        val echo = new Echo()
        val server = new GatewayServer(echo)
        server.start()
    }
}