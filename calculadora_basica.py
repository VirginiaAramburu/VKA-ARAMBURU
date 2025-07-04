def suma(*nums: float) -> float:
    return sum(nums)

def resta(*nums: float) -> float:
    if not nums:
        return 0
    res = nums[0]
    for valor in nums[1:]:
        res -= valor
    return res

def mult(*nums: float) -> float:
    res = 1
    for valor in nums:
        res *= valor
    return res

def div(n1: float, n2: float) -> tuple:
    if n2 == 0:
        return "Error: División por cero"
    return n1 / n2, n1 % n2

def main():
    print("Calculadora simple")
    print("Operaciones disponibles: suma, resta, mult, div")
    operacion = input("¿Qué operación deseas realizar? ").strip().lower()

    if operacion in ["suma", "resta", "mult"]:
        numeros = input("Introduce los números separados por espacio: ")
        nums = list(map(float, numeros.split()))
        if operacion == "suma":
            print("Resultado:", suma(*nums))
        elif operacion == "resta":
            print("Resultado:", resta(*nums))
        elif operacion == "mult":
            print("Resultado:", mult(*nums))
    elif operacion == "div":
        n1 = float(input("Introduce el dividendo: "))
        n2 = float(input("Introduce el divisor: "))
        resultado = div(n1, n2)
        print("Resultado:", resultado)
    else:
        print("Operación no válida.")

if __name__ == "__main__":
    main()
