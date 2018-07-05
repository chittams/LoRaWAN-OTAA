numADCreadings = const(100)
class battery(object):
    def status():
        import machine
        from machine import ADC
        adc = ADC(0)
        adcread = adc.channel(attn=3, pin='P16')
        samplesADC = [0.0]*numADCreadings; meanADC = 0.0
        count = 0
        while (count < numADCreadings):
            adcint = adcread()
            samplesADC[count] = adcint
            meanADC += adcint
            count += 1
        meanADC /= numADCreadings
        varianceADC = 0.0
        for adcint in samplesADC:
            varianceADC += (adcint - meanADC)**2
        varianceADC /= (numADCreadings - 1)
        mV = meanADC*1400/1024
        return mV