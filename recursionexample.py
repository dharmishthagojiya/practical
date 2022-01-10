def sumoflist(n):
    if len(n)==1:
        return n[0]
    else:
      return n[0] + sumoflist(n[1:])
print(sumoflist([1,20,56,34,2]))
#convert interger to string
def to_string(n,base):#2815
    convert="0123456789ABCDEF"
    if n<base:#2815<16
        return convert[n]
    else: #2815//16,16 +15,,,,(175//16,15)
        return to_string(n//base,base)+convert[n%base]
print(to_string(2845,16))
print(2815//16)
#sum of digit
def sumofdig(n) :
    if n == 0:
        return 0
    else:
        return (n%10)+sumofdig(int(n/10))
print("sum of digit",sumofdig((123)))
#sumof series
def sum_series(n):
    if n<0:
        return 0
    else:
        return n+sum_series(n-2)
print("sum of series",sum_series(8))#8+6+4+2+0
#harmonic sum
def harmonic(n):
    if n==0:
        return 0
    else:
        return 1/n+harmonic(n-1)
print("harmonic",harmonic(10))
#gometric serie
def geometric_sum(n):
    if n < 0:
        return 0
    else:
        return 1 / (pow(4, n)) + geometric_sum(n - 1)
print(geometric_sum(7))
print(geometric_sum(4))

