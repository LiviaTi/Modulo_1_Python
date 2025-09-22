import cowsay
def greeting(name: str='42') -> None:
    """
    receives a name and prints a greeting
    """
    cowsay.meow(f"Hello {name}")
