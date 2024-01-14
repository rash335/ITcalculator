import numpy as np
import numpy as np

netCTC = 1823730;
pf = 7295;
reducedCTC = netCTC - pf*12

bonusReceived = 61400;
CTCwithBonus = bonusReceived*12/0.7 + reducedCTC;

DeducStd = 50000;
Deduc80c = 149188;
Deduc80d = 34701;
netTaxableInc = CTCwithBonus - (DeducStd + Deduc80c + Deduc80d)

if netTaxableInc >= 0 and netTaxableInc < 250000:
    tax1 = 0;
else: tax1 = 0;
    
if netTaxableInc >= 250000 and netTaxableInc < 500000:
    tax2 = 0.025 * (netTaxableInc - 250000) + tax1;
else: tax2 = 0.025 * 250000 + tax1;
    
if netTaxableInc >= 500000 and netTaxableInc < 1000000:
    tax3 = 0.2 * (netTaxableInc - 500000) + tax2 + tax1;
else: tax3 = 0.2 * 500000 + tax2 + tax1;

if netTaxableInc >= 1000000:
    tax4 = 0.3 * (netTaxableInc - 1000000) + tax3 + tax2 + tax1;

healthCess = 0.02 * tax4
