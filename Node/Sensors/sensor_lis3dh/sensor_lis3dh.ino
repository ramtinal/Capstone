#include <TinyPICO.h>
#include <Wire.h>
#include <SPI.h>
#include <Adafruit_LIS3DH.h>
#include <Adafruit_Sensor.h>

#define LIS3DH_CS 5    //SS
#define LIS3DH_CLK 18   //SCL
#define LIS3DH_MISO 19  //SDO
#define LIS3DH_MOSI 23  //SDA

Adafruit_LIS3DH lis = Adafruit_LIS3DH(LIS3DH_CS, LIS3DH_MOSI, LIS3DH_MISO, LIS3DH_CLK);

// Initialise the TinyPICO library
TinyPICO tp = TinyPICO();

void setup()
{
    // Used for debug output only
    Serial.begin(115200);
    while (!Serial) delay(10); //Pause until the console opens

    Serial.println("LIS3DH Node Development\n");
    Serial.print("PICO Battery Voltage is: ");
    Serial.println(tp.GetBatteryVoltage());
    Serial.print("PICO Battery Charge State is: ");
    Serial.println(tp.IsChargingBattery());

    if(!lis.begin()) {
      Serial.println("Couldn't start");
      while(1) yield();
    }

    lis.setRange(LIS3DH_RANGE_2_G); //2,4,8, or 16G

    Serial.print("Range = "); Serial.print(2<<lis.getRange()); Serial.println("G");

    lis.setDataRate(LIS3DH_DATARATE_50_HZ);
    Serial.print("Data rate = ");
    switch (lis.getDataRate()) {
      case LIS3DH_DATARATE_1_HZ: Serial.println("1 Hz"); break;
      case LIS3DH_DATARATE_10_HZ: Serial.println("10 Hz"); break;
      case LIS3DH_DATARATE_25_HZ: Serial.println("25 Hz"); break;
      case LIS3DH_DATARATE_50_HZ: Serial.println("50 Hz"); break;
      case LIS3DH_DATARATE_100_HZ: Serial.println("100 Hz"); break;
      case LIS3DH_DATARATE_200_HZ: Serial.println("200 Hz"); break;
      case LIS3DH_DATARATE_400_HZ: Serial.println("400 Hz"); break;

      case LIS3DH_DATARATE_POWERDOWN: Serial.println("Powered Down"); break;
      case LIS3DH_DATARATE_LOWPOWER_5KHZ: Serial.println("5kHz Low Power"); break;
      case LIS3DH_DATARATE_LOWPOWER_1K6HZ: Serial.println("16kHz Low Power"); break;
    }
}

void loop() {
  lis.read();      // get X Y and Z data at once
  // Then print out the raw data
  Serial.print("X:  "); Serial.print(lis.x);
  Serial.print("  \tY:  "); Serial.print(lis.y);
  Serial.print("  \tZ:  "); Serial.print(lis.z);

  /* Or....get a new sensor event, normalized */
  sensors_event_t event;
  lis.getEvent(&event);

  /* Display the results (acceleration is measured in m/s^2) */
  Serial.print("\t\tX: "); Serial.print(event.acceleration.x);
  Serial.print(" \tY: "); Serial.print(event.acceleration.y);
  Serial.print(" \tZ: "); Serial.print(event.acceleration.z);
  Serial.println(" m/s^2 ");

  Serial.println();

  delay(200);
}
