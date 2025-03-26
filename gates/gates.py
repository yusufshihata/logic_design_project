
class Gates:
    def __init__(self):
        pass

    @staticmethod
    def and_gate(*args):
        result = args[0]
        for i in range(1, len(args)):
            result = result and args[i]
        return result

    @staticmethod
    def or_gate(*args):
        result = args[0]
        for i in range(1, len(args)):
            result = result or args[i]
        return result

    @staticmethod
    def not_gate(a):
        return not a
    
    @staticmethod
    def nand_gate(*args):
        return Gates.not_gate(Gates.and_gate(*args))

    @staticmethod
    def nor_gate(*args):
        return Gates.not_gate(Gates.or_gate(*args))
    
    @staticmethod
    def xor_gate(*args):
        result = args[0]
        for i in range(1, len(args)):
            result = Gates.and_gate(Gates.or_gate(result, args[i]), Gates.nand_gate(result, args[i]))
        return result

    @staticmethod
    def xnor_gate(*args):
        return Gates.not_gate(Gates.xor_gate(*args))
