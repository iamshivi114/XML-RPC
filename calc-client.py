import xmlrpc.client
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python calc_client.py <server> <port>")
        sys.exit(1)
    server, port = sys.argv[1], int(sys.argv[2])
    url = f"http://{server}:{port}/RPC"
    proxy = xmlrpc.client.ServerProxy(url)

    try:
        print("subtract(12, 6) =", proxy.subtract(12, 6))
        print("multiply(3, 4) =", proxy.multiply(3, 4))
        print("divide(10, 5) =", proxy.divide(10, 5))
        print("modulo(10, 5) =", proxy.modulo(10, 5))
        print("add(0) =", proxy.add(0))
        print("add(1, 2, 3, 4, 5) =", proxy.add(1, 2, 3, 4, 5))
        print("multiply(1, 2, 3, 4, 5) =", proxy.multiply(1, 2, 3, 4, 5))

        try:
            print("add overflow:", proxy.add(sys.maxsize, sys.maxsize))
            print("multiply overflow:", proxy.multiply(sys.maxsize, sys.maxsize))
            print("subtract with string arguments:", proxy.subtract("a", "b"))
            print("divide by zero:", proxy.divide(10, 0))
        except xmlrpc.client.Fault as e:
            print("XML-RPC Fault:", e)
        except Exception as e:
            print("Error:", e)

    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    main()
