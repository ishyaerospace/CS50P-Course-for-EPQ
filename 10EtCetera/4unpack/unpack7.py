def f(*args, **kwargs): # convention of placeholder would be args=arguments, kwargs=keywork arguments
    print("Positional:", kwargs)

f(galleons=100, sickles=50, knuts=25) #kwargs is a dictionary
