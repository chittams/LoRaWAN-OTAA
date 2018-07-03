import machine

class Battery:
    numADCreadings = const(100)

    def __init__(self):
        self.adc = machine.ADC(0)
        self.adcread = self.adc.channel(attn=3, pin='P16')
        self.samplesADC = [0.0]*numADCreadings
        self.meanADC = 0.0

    def checkLow(self):
        voltage = status() * 1000
        if(status() < 3.8):
            return True
        return False

    def status():
        count = 0
        while (count < numADCreadings):
            adcint = self.adcread()
            self.samplesADC[count] = adcint
            self.meanADC += adcint
            count += 1
        self.meanADC /= numADCreadings
        varianceADC = 0.0
        for adcint in self.samplesADC:
            varianceADC += (adcint - self.meanADC)**2
        varianceADC /= (numADCreadings - 1)
        mV = self.meanADC*1400/1024
        return mV