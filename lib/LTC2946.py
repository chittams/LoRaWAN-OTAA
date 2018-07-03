# LTC2946 default address.
LTC2946_I2CADDR = 0x6F

# Registers
LTC2946_CTRLA_REG                          = 0x00
LTC2946_CTRLB_REG                          = 0x01
LTC2946_ALERT1_REG                         = 0x02
LTC2946_STATUS1_REG                        = 0x03
LTC2946_FAULT1_REG                         = 0x04

LTC2946_POWER_MSB2_REG                     = 0x05
LTC2946_POWER_MSB1_REG                     = 0x06
LTC2946_POWER_LSB_REG                      = 0x07
LTC2946_MAX_POWER_MSB2_REG                 = 0x08
LTC2946_MAX_POWER_MSB1_REG                 = 0x09
LTC2946_MAX_POWER_LSB_REG                  = 0x0A
LTC2946_MIN_POWER_MSB2_REG                 = 0x0B
LTC2946_MIN_POWER_MSB1_REG                 = 0x0C
LTC2946_MIN_POWER_LSB_REG                  = 0x0D
LTC2946_MAX_POWER_THRESHOLD_MSB2_REG       = 0x0E
LTC2946_MAX_POWER_THRESHOLD_MSB1_REG       = 0x0F
LTC2946_MAX_POWER_THRESHOLD_LSB_REG        = 0x10
LTC2946_MIN_POWER_THRESHOLD_MSB2_REG       = 0x11
LTC2946_MIN_POWER_THRESHOLD_MSB1_REG       = 0x12
LTC2946_MIN_POWER_THRESHOLD_LSB_REG        = 0x13

LTC2946_DELTA_SENSE_MSB_REG                = 0x14
LTC2946_DELTA_SENSE_LSB_REG                = 0x15
LTC2946_MAX_DELTA_SENSE_MSB_REG            = 0x16
LTC2946_MAX_DELTA_SENSE_LSB_REG            = 0x17
LTC2946_MIN_DELTA_SENSE_MSB_REG            = 0x18
LTC2946_MIN_DELTA_SENSE_LSB_REG            = 0x19
LTC2946_MAX_DELTA_SENSE_THRESHOLD_MSB_REG  = 0x1A
LTC2946_MAX_DELTA_SENSE_THRESHOLD_LSB_REG  = 0x1B
LTC2946_MIN_DELTA_SENSE_THRESHOLD_MSB_REG  = 0x1C
LTC2946_MIN_DELTA_SENSE_THRESHOLD_LSB_REG  = 0x1D

LTC2946_VIN_MSB_REG                        = 0x1E
LTC2946_VIN_LSB_REG                        = 0x1F
LTC2946_MAX_VIN_MSB_REG                    = 0x20
LTC2946_MAX_VIN_LSB_REG                    = 0x21
LTC2946_MIN_VIN_MSB_REG                    = 0x22
LTC2946_MIN_VIN_LSB_REG                    = 0x23
LTC2946_MAX_VIN_THRESHOLD_MSB_REG          = 0x24
LTC2946_MAX_VIN_THRESHOLD_LSB_REG          = 0x25
LTC2946_MIN_VIN_THRESHOLD_MSB_REG          = 0x26
LTC2946_MIN_VIN_THRESHOLD_LSB_REG          = 0x27

LTC2946_ADIN_MSB_REG                       = 0x28
LTC2946_ADIN_LSB_REG_REG                   = 0x29
LTC2946_MAX_ADIN_MSB_REG                   = 0x2A
LTC2946_MAX_ADIN_LSB_REG                   = 0x2B
LTC2946_MIN_ADIN_MSB_REG                   = 0x2C
LTC2946_MIN_ADIN_LSB_REG                   = 0x2D
LTC2946_MAX_ADIN_THRESHOLD_MSB_REG         = 0x2E
LTC2946_MAX_ADIN_THRESHOLD_LSB_REG         = 0x2F
LTC2946_MIN_ADIN_THRESHOLD_MSB_REG         = 0x30
LTC2946_MIN_ADIN_THRESHOLD_LSB_REG         = 0x31

LTC2946_ALERT2_REG                         = 0x32
LTC2946_GPIO_CFG_REG                       = 0x33

LTC2946_TIME_COUNTER_MSB3_REG              = 0x34
LTC2946_TIME_COUNTER_MSB2_REG              = 0x35
LTC2946_TIME_COUNTER_MSB1_REG              = 0x36
LTC2946_TIME_COUNTER_LSB_REG               = 0x37

LTC2946_CHARGE_MSB3_REG                    = 0x38
LTC2946_CHARGE_MSB2_REG                    = 0x39
LTC2946_CHARGE_MSB1_REG                    = 0x3A
LTC2946_CHARGE_LSB_REG                     = 0x3B

LTC2946_ENERGY_MSB3_REG                    = 0x3C
LTC2946_ENERGY_MSB2_REG                    = 0x3D
LTC2946_ENERGY_MSB1_REG                    = 0x3E
LTC2946_ENERGY_LSB_REG                     = 0x3F

LTC2946_STATUS2_REG                        = 0x40
LTC2946_FAULT2_REG                         = 0x41
LTC2946_GPIO3_CTRL_REG                     = 0x42
LTC2946_CLK_DIV_REG                        = 0x43


# Voltage Selection Command
LTC2946_DELTA_SENSE                        = 0x00
LTC2946_VDD                                = 0x08
LTC2946_ADIN                               = 0x10
LTC2946_SENSE_PLUS                         = 0x18

# Command Codes
LTC2946_ADIN_INTVCC                        = 0x80
LTC2946_ADIN_GND                           = 0x00

LTC2946_OFFSET_CAL_LAST                    = 0x60
LTC2946_OFFSET_CAL_128                     = 0x40
LTC2946_OFFSET_CAL_16                      = 0x20
LTC2946_OFFSET_CAL_EVERY                   = 0x00

LTC2946_CHANNEL_CONFIG_SNAPSHOT            = 0x07
LTC2946_CHANNEL_CONFIG_V_C                 = 0x06
LTC2946_CHANNEL_CONFIG_A_V_C_1             = 0x05
LTC2946_CHANNEL_CONFIG_A_V_C_2             = 0x04
LTC2946_CHANNEL_CONFIG_A_V_C_3             = 0x03
LTC2946_CHANNEL_CONFIG_V_C_1               = 0x02
LTC2946_CHANNEL_CONFIG_V_C_2               = 0x01
LTC2946_CHANNEL_CONFIG_V_C_3               = 0x00

LTC2946_ENABLE_ALERT_CLEAR                 = 0x80
LTC2946_ENABLE_SHUTDOWN                    = 0x40
LTC2946_ENABLE_CLEARED_ON_READ             = 0x20
LTC2946_ENABLE_STUCK_BUS_RECOVER           = 0x10

LTC2946_DISABLE_ALERT_CLEAR                = 0x7F
LTC2946_DISABLE_SHUTDOWN                   = 0xBF
LTC2946_DISABLE_CLEARED_ON_READ            = 0xDF
LTC2946_DISABLE_STUCK_BUS_RECOVER          = 0xEF

LTC2946_ACC_PIN_CONTROL                    = 0x08
LTC2946_DISABLE_ACC                        = 0x04
LTC2946_ENABLE_ACC                         = 0x00

LTC2946_RESET_ALL                          = 0x03
LTC2946_RESET_ACC                          = 0x02
LTC2946_ENABLE_AUTO_RESET                  = 0x01
LTC2946_DISABLE_AUTO_RESET                 = 0x00

LTC2946_MAX_POWER_MSB2_RESET               = 0x00
LTC2946_MIN_POWER_MSB2_RESET               = 0xFF
LTC2946_MAX_DELTA_SENSE_MSB_RESET          = 0x00
LTC2946_MIN_DELTA_SENSE_MSB_RESET          = 0xFF
LTC2946_MAX_VIN_MSB_RESET                  = 0x00
LTC2946_MIN_VIN_MSB_RESET                  = 0xFF
LTC2946_MAX_ADIN_MSB_RESET                 = 0x00
LTC2946_MIN_ADIN_MSB_RESET                 = 0xFF

LTC2946_ENABLE_MAX_POWER_ALERT             = 0x80
LTC2946_ENABLE_MIN_POWER_ALERT             = 0x40
LTC2946_DISABLE_MAX_POWER_ALERT            = 0x7F
LTC2946_DISABLE_MIN_POWER_ALERT            = 0xBF

LTC2946_ENABLE_MAX_I_SENSE_ALERT           = 0x20
LTC2946_ENABLE_MIN_I_SENSE_ALERT           = 0x10
LTC2946_DISABLE_MAX_I_SENSE_ALERT          = 0xDF
LTC2946_DISABLE_MIN_I_SENSE_ALERT          = 0xEF

LTC2946_ENABLE_MAX_VIN_ALERT               = 0x08
LTC2946_ENABLE_MIN_VIN_ALERT               = 0x04
LTC2946_DISABLE_MAX_VIN_ALERT              = 0xF7
LTC2946_DISABLE_MIN_VIN_ALERT              = 0xFB

LTC2946_ENABLE_MAX_ADIN_ALERT              = 0x02
LTC2946_ENABLE_MIN_ADIN_ALERT              = 0x01
LTC2946_DISABLE_MAX_ADIN_ALERT             = 0xFD
LTC2946_DISABLE_MIN_ADIN_ALERT             = 0xFE

LTC2946_ENABLE_ADC_DONE_ALERT              = 0x80
LTC2946_DISABLE_ADC_DONE_ALERT             = 0x7F

LTC2946_ENABLE_GPIO_1_ALERT                = 0x40
LTC2946_DISABLE_GPIO_1_ALERT               = 0xBF

LTC2946_ENABLE_GPIO_2_ALERT                = 0x20
LTC2946_DISABLE_GPIO_2_ALERT               = 0xDF

LTC2946_ENABLE_STUCK_BUS_WAKE_ALERT        = 0x08
LTC2946_DISABLE_STUCK_BUS_WAKE_ALERT       = 0xF7

LTC2946_ENABLE_ENERGY_OVERFLOW_ALERT       = 0x04
LTC2946_DISABLE_ENERGY_OVERFLOW_ALERT      = 0xFB

LTC2946_ENABLE_CHARGE_OVERFLOW_ALERT       = 0x02
LTC2946_DISABLE_CHARGE_OVERFLOW_ALERT      = 0xFD

LTC2946_ENABLE_COUNTER_OVERFLOW_ALERT      = 0x01
LTC2946_DISABLE_COUNTER_OVERFLOW_ALERT     = 0xFE

LTC2946_GPIO1_IN_ACTIVE_HIGH               = 0xC0
LTC2946_GPIO1_IN_ACTIVE_LOW                = 0x80
LTC2946_GPIO1_OUT_HIGH_Z                   = 0x40
LTC2946_GPIO1_OUT_LOW                      = 0x00

LTC2946_GPIO2_IN_ACTIVE_HIGH               = 0x30
LTC2946_GPIO2_IN_ACTIVE_LOW                = 0x20
LTC2946_GPIO2_OUT_HIGH_Z                   = 0x10
LTC2946_GPIO2_OUT_LOW                      = 0x12
LTC2946_GPIO2_IN_ACC                       = 0x00

LTC2946_GPIO3_IN_ACTIVE_HIGH               = 0x0C
LTC2946_GPIO3_IN_ACTIVE_LOW                = 0x08
LTC2946_GPIO3_OUT_REG_42                   = 0x04
LTC2946_GPIO3_OUT_ALERT                    = 0x00
LTC2946_GPIO3_OUT_LOW                      = 0x40
LTC2946_GPIO3_OUT_HIGH_Z                   = 0x00
LTC2946_GPIO_ALERT_CLEAR                   = 0x00

# Register Mask Command
LTC2946_CTRLA_ADIN_MASK                    = 0x7F
LTC2946_CTRLA_OFFSET_MASK                  = 0x9F
LTC2946_CTRLA_VOLTAGE_SEL_MASK             = 0xE7
LTC2946_CTRLA_CHANNEL_CONFIG_MASK          = 0xF8
LTC2946_CTRLB_ACC_MASK                     = 0xF3
LTC2946_CTRLB_RESET_MASK                   = 0xFC
LTC2946_GPIOCFG_GPIO1_MASK                 = 0x3F
LTC2946_GPIOCFG_GPIO2_MASK                 = 0xCF
LTC2946_GPIOCFG_GPIO3_MASK                 = 0xF3
LTC2946_GPIOCFG_GPIO2_OUT_MASK             = 0xFD
LTC2946_GPIO3_CTRL_GPIO3_MASK              = 0xBF

# LSB Weights
const float LTC2946_ADIN_lsb = 5.001221E-04;                      #!< Typical ADIN lsb weight in volts
const float LTC2946_DELTA_SENSE_lsb = 2.5006105E-05;              #!< Typical Delta lsb weight in volts
const float LTC2946_VIN_lsb = 2.5006105E-02;                      #!< Typical VIN lsb weight in volts
const float LTC2946_Power_lsb = 6.25305E-07;                      #!< Typical POWER lsb weight in V^2 VIN_lsb * DELTA_SENSE_lsb
const float LTC2946_ADIN_DELTA_SENSE_lsb = 1.25061E-08;           #!< Typical sense lsb weight in V^2  *ADIN_lsb * DELTA_SENSE_lsb
const float LTC2946_INTERNAL_TIME_lsb = 4101.00/250000.00;        #!< Internal TimeBase lsb. Use LTC2946_TIME_lsb if an external CLK is used. See Settings menu for how to calculate Time LSB.

class LTC2946:

    def __init__(self, address=LTC2946_I2CADDR, i2c=None):
        # Create I2C device.
        if i2c is None:
            raise ValueError('Error I2C object is required.')
        # Create device, catch permission errors

        self.i2c = i2c
        self.address = address
        result = self.address in self.i2c.scan()
        if result is False:
            print("Unable to communicate with sensor, check connections.")
            exit()

        import Adafruit_GPIO.I2C as I2C

        self._device = I2C.Device(address, i2c)

    #! SENSE+ - Snapshot mode
    def read_voltage(self):
        LTC2946_mode = (LTC2946_CHANNEL_CONFIG_SNAPSHOT | LTC2946_SENSE_PLUS)
        self._device.write8(LTC2946_CTRLA_REG, LTC2946_mode)
        
        while (0x8 & busy)
            busy = self._device.read8(LTC2946_STATUS2_REG)
        
        voltage_code = self._device.readS16(LTC2946_VIN_MSB_REG)
        voltage = voltage_code * LTC2946_VIN_lsb
        return voltage

    #! ADIN - Snapshot Mode
    def read_ADIN(self, scale):
        LTC2946_mode = LTC2946_CHANNEL_CONFIG_SNAPSHOT | LTC2946_ADIN
        self._device.write8(LTC2946_CTRLA_REG, LTC2946_mode)

        while (0x8 & busy)
            busy = self._device.read8(LTC2946_STATUS2_REG)

        ADIN_code = self._device.readS16(LTC2946_ADIN_MSB_REG)
        max_ADIN_code = self._device.readS16(LTC2946_MAX_ADIN_MSB_REG)
        min_ADIN_code = self._device.readS16(LTC2946_MIN_ADIN_MSB_REG)
        ADIN = ADIN_code * LTC2946_ADIN_lsb * scale
        max_ADIN = max_ADIN_code * LTC2946_ADIN_lsb * scale
        min_ADIN = min_ADIN_code * LTC2946_ADIN_lsb * scale
        return ADIN,max_ADIN,min_ADIN
    
    #! VDD - Snapshot Mode
    def read_VDD(self):
        LTC2946_mode = LTC2946_CHANNEL_CONFIG_SNAPSHOT | LTC2946_VDD
        self._device.write8(LTC2946_CTRLA_REG, LTC2946_mode)

        while (0x8 & busy)
            busy = self._device.read8(LTC2946_STATUS2_REG)

        VDD_code = self._device.readS16(LTC2946_VIN_MSB_REG)
        VDD = VDD_code * LTC2946_VIN_lsb
        return VDD
    
    #! Current - Snapshot Mode
    def read_Current(self):
        LTC2946_mode = LTC2946_CHANNEL_CONFIG_SNAPSHOT | LTC2946_DELTA_SENSE
        self._device.write8(LTC2946_CTRLA_REG, LTC2946_mode)

        while (0x8 & busy)
            busy = self._device.read8(LTC2946_STATUS2_REG)

        current_code = self._device.readS16(LTC2946_DELTA_SENSE_MSB_REG)
        max_current_code = self._device.readS16(LTC2946_MAX_DELTA_SENSE_MSB_REG)
        min_current_code = self._device.readS16(LTC2946_MIN_DELTA_SENSE_MSB_REG)
        
        current = current_code * LTC2946_DELTA_SENSE_lsb
        max_current = max_current_code * LTC2946_DELTA_SENSE_lsb
        min_current = min_current_code * LTC2946_DELTA_SENSE_lsb);
        return current,max_current,min_current