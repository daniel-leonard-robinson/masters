#include "header.h"

// #define bufLen 2000
// uint16_t aCounter = 0;
// uint32_t prevMillis = 0;
// uint8_t analogBuf[bufLen];
volatile uint32_t tStart, tEnd, sum = 0, idleTime = 0, txTime = 0, tOffset = 0, tStep = 0;
volatile uint32_t zeroCounter = 0, readCount = 0, zeroM = 0, tStepCount = 0;
volatile double energy = 0;
uint32_t maxReading = 0;
// boolean prime = false;

char tx[64];
BufferSerial buf(tx, 64);

void energySetup() {
    sum = idleTime = txTime = readCount = maxReading = energy = tStepCount = 0;
}

void energyFlush() {
    buf.flush();
    tx[0] = '\0';
    // buf.print(buf.current_length());
    // buf.print(',');
}

void energyPrint() {
    Serial.print(buf);
    // Serial.print((const char *)tx);
}

void energyLoop(boolean pause) {
    uint8_t reading = analogRead(A0);
    if (reading > 60) {
        // Serial.println(reading);
        if (reading > maxReading) maxReading = reading;
        if (!readCount++) {
            tStart = millis();
            idleTime = tStart - tEnd;
        }
        tEnd = millis();
        zeroM = tEnd;
        zeroCounter = 0;
        sum += reading;
        tStepCount += micros() - tStep;
    }
    // else if (zeroCounter < 5000) {
    //     if (pause) zeroCounter = 1;
    //     zeroCounter++;
    // }
    else if (pause) zeroM = millis();
    else if (millis() - zeroM < 1000);
    else if (readCount) {
        txTime = tEnd - tStart;
        tStepCount /= 1000;
        energy = sum * 500 / 1023.0 * tStepCount / 1000 / 1000;
        
        energyFlush();

        buf.print(idleTime); buf.print(",");
        buf.print(txTime); buf.print(",");
        buf.print(tStepCount); buf.print(",");
        buf.print(energy); buf.print(",");
        buf.println(maxReading/2);

        energyPrint();
        energySetup();
    }

    tStep = micros();
}