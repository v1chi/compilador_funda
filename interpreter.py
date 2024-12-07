
#entorno
class Environment:
    def __init__(self):
        self.variables = {}

    def get(self, name):
        return self.variables.get(name, None)

    def set(self, name, value):
        self.variables[name] = value


#para evaluar todas las operaciones aritmeticas y logicas y las llamadas de funciones
def evaluate_expression(expr, env):
    try:
        if isinstance(expr, tuple):
            op = expr[0]
            if op == 'add':
                return evaluate_expression(expr[1], env) + evaluate_expression(expr[2], env)
            elif op == 'subtract':
                return evaluate_expression(expr[1], env) - evaluate_expression(expr[2], env)
            elif op == 'multiply':
                return evaluate_expression(expr[1], env) * evaluate_expression(expr[2], env)
            elif op == 'divide':
                return evaluate_expression(expr[1], env) / evaluate_expression(expr[2], env)
            elif op == 'mod':
                return evaluate_expression(expr[1], env) % evaluate_expression(expr[2], env)
            elif op == 'call':
                func_name = expr[1]
                args = [evaluate_expression(arg, env) for arg in expr[2]]
                return call_function(func_name, args, env)
            elif op == '>':
                return evaluate_expression(expr[1], env) > evaluate_expression(expr[2], env)
            elif op == '<':
                return evaluate_expression(expr[1], env) < evaluate_expression(expr[2], env)
            elif op == '==':
                return evaluate_expression(expr[1], env) == evaluate_expression(expr[2], env)
            elif op == 'and':
                return evaluate_expression(expr[1], env) and evaluate_expression(expr[2], env)
            elif op == 'or':
                return evaluate_expression(expr[1], env) or evaluate_expression(expr[2], env)
        elif isinstance(expr, str):
            value = env.get(expr)
            if value is not None:
                return value
            else:
                return expr  # Es una cadena de texto
        else:
            return expr
    except TypeError as e:
        print(f"Error: {e}")
        return None

# declarar variables y funciones, prints, condicional y bucle
def execute_declaration(decl, env):
    try:
        if decl[0] == 'declare':
            _, var_type, var_name, expr = decl
            value = evaluate_expression(expr, env)
            env.set(var_name, value)
        elif decl[0] == 'out':
            value = evaluate_expression(decl[1], env)
            print(value)
        elif decl[0] == 'function':
            _, func_name, params, body, return_stmt = decl
            env.set(func_name, (params, body, return_stmt))
        elif decl[0] == 'if':
            _, condition, then_body = decl
            if evaluate_expression(condition, env):
                execute_declarations(then_body, env)
        elif decl[0] == 'if_else':
            _, condition, then_body, else_body = decl
            if evaluate_expression(condition, env):
                execute_declarations(then_body, env)
            else:
                execute_declarations(else_body, env)
        elif decl[0] == 'loop':
            _, var_name, start_expr, end_expr, body = decl
            start = evaluate_expression(start_expr, env)
            end = evaluate_expression(end_expr, env)
            for i in range(start, end + 1):
                env.set(var_name, i)
                execute_declarations(body, env)
    except Exception as e:
        print(f"Error: {e}")

#ejecutar declaraciones
def execute_declarations(decls, env):
    for decl in decls:
        execute_declaration(decl, env)

#llamar funcion
def call_function(func_name, args, env):
    try:
        func = env.get(func_name)
        if func:
            params, body, return_stmt = func
            local_env = Environment()
            local_env.variables.update(env.variables)  
            for (param_type, param_name), arg in zip(params, args):
                local_env.set(param_name, arg)
            execute_declarations(body, local_env)
            if return_stmt:
                return evaluate_expression(return_stmt[1], local_env)
        else:
            raise Exception(f"funcion {func_name} no definifa")
    except Exception as e:
        print(f"Error debido a : {e}")
        return None