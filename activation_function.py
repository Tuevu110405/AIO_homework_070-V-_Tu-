#function for computing F1 score
def compute_F1_score(tp, fp, fn):
    precision, recall, f1_score= 0, 0, 0
    if type(tp) != int :
        print('tp must be int')
    elif type(fp) != int :
        print('fp must be int')
    elif type(fn) != int :
        print('fn must be int')
    elif tp <=0 or fp <= 0 or fn <= 0:
        print('tp and fp and fn must be greater than zero')
    else:
        precision = tp/(tp +fp)
        recall = tp/(tp +fn)
        f1_score = 2* (precision* recall)/ (precision+ recall)
        return precision, recall, f1_score
    

import math
import numbers

def is_number(var):
    return isinstance(var, numbers.Number)


#function for signmoid, relu, and elu
def activation_function (f_name, x):
    #check number
    if is_number(x) == False:
        print('x must be a number')
        return False
    else:
        x = float(x)

    #compute f(x)
    if f_name == 'sigmoid':
        sigmoid = 1/(1+ math.exp(-x))
        return sigmoid
    elif f_name == 'relu':
        if x <= 0:
            return 0
        else:
            return x
    elif f_name == 'ELU':
        if x <= 0:
            elu = 0.01*(math.exp(x)- 1)
        else:
            elu = x
        return elu
    else:
        print('function_name is not supported')
        return False


import random

#Computing loss
def compute_loss(f_name,n):
    target = [] 
    predict = []
    
    if n.isnumeric() != True:
        print('number of samples must be an integer number')
        return False
    else:
        n = int(n)
    
    for i in range(n):
        target.append(random.uniform(0, 10))
        predict.append(random.uniform(0, 10))
    
    f_name = f_name.lower()
    if f_name == 'mae':
        sum1 = 0
        for i in range(n):
            sum1 += math.fabs(target[i]-predict[i])
        f1 = sum1 / n
        return f1
    elif f_name == 'mse':
        sum2 = 0
        for i in range(n):
            sum2 += (target[i]-predict[i])**2
        f2 = sum2 / n
        return f2
    elif f_name == 'rmse':
        sum3 = 0
        for i in range(n):
            sum3 += (target[i]-predict[i])**2
        f3 = math.sqrt(sum3 / n)
        return f3
    else:
        print('function is not supported')
        return False


# factorial function
def factorial(x):
    if x == 0:
        return 1
    else:
        return factorial(x-1)*x


#maclaurin compute sin
def compute_sin(x, n):
    sin = 0
    for i in range(n):
        sin += ((-1)**i)*(x**(2*i+1))/factorial(2*i+1)
    return sin

#compute cos
def compute_cos(x, n):
    cos = 0
    for i in range(n):
        cos += ((-1)**i)*(x**(2*i))/factorial(2*i)
    return cos


#compute sinh
def compute_sinh(x,n):
    sinh = 0
    for i in range(n):
        sinh += x**(2*i+1)/ factorial(2*i + 1)
    return sinh


#compute cosh
def compute_cosh(x, n):
    cosh = 0
    for i in range(n):
        cosh += x**(2*i)/ factorial(2*i)
    return cosh


#compute MD_nRE
def md_nre(y, y_hat, n, p):
    result = (y**(1/n) - y_hat**(1/n))**p
    return result