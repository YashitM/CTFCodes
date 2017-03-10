'''
Created on Dec 14, 2011

@author: pablocelayes
'''

import ContinuedFractions, Arithmetic, RSAvulnerableKeyGenerator

def hack_RSA(e,n):
    '''
    Finds d knowing (e,n)
    applying the Wiener continued fraction attack
    '''
    frac = ContinuedFractions.rational_to_contfrac(e, n)
    convergents = ContinuedFractions.convergents_from_contfrac(frac)
    
    for (k,d) in convergents:
        
        #check if d is actually the key
        if k!=0 and (e*d-1)%k == 0:
            phi = (e*d-1)//k
            s = n - phi + 1
            # check if the equation x^2 - s*x + n = 0
            # has integer roots
            discr = s*s - 4*n
            if(discr>=0):
                t = Arithmetic.is_perfect_square(discr)
                if t!=-1 and (s+t)%2==0:
                    print("Hacked!")
                    return d
		else:
			print("failed")
	    else:
		print("failed")


n=549100898763808112064590568096509639806005267015788479836998648112330729762142760306265813195181231930171220686827142359040315653020182064933039077953579528749272321744478656324986362155106653831095037724728643255316641716947998245610175805278242802144980117927688674393383290354985820646326870614197414534217177211618710501438340081867982883181358830449072661742417246835970022211465130756382481343160426921258769780282358703413114522476037306476452786236456339806564839822630841425055758411765631749632457527073092742671445828538125416154242015006557099276782924659662805070769995499831691512789480191593818008294274869515824359702140052678892212293539574359134092465336347101950176544334845468112561615253963771393076343090247719105323352711194948081670662350809687853687199699436636944300210595489981211181100443706510898137733979941302306471697516217631493070094434891637922047009630278889176140288479340611479190580909389486067761958499091506601085734094801729179308537628951345012578144960250844126260353636619225347430788141190654302935255862518781845236444151680147886477815759103864509989480675169631226254252762579781553994364555800120817100328166428687776427164098803076677481602221304265962340500651339469391627432175447
e=65537

hack_RSA(e,n)




# TEST functions

"""
def test_hack_RSA():
    print("Testing Wiener Attack")
    times = 5
    
    while(times>0):
        e,n,d = RSAvulnerableKeyGenerator.generateKeys(1024)
        print("(e,n) is (", e, ", ", n, ")")
        print("d = ", d)
    
        hacked_d = hack_RSA(e, n)
    
        if d == hacked_d:
            print("Hack WORKED!")
        else:
            print("Hack FAILED")
        
        print("d = ", d, ", hacked_d = ", hacked_d)
        print("-------------------------")
        times -= 1
"""
"""    
if __name__ == "__main__":
    #test_is_perfect_square()
    #print("-------------------------")
    test_hack_RSA()

"""
    


        
    
