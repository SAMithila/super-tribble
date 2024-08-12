def func(i, n):
    if i > n:
        return
    print("Raj")
    func(i + 1, n)

def main():
    n = int(input("Enter a number: "))
    func(1, n)

main()

