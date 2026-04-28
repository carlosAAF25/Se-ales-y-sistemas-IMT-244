
const int FILTER_ORDER = 10;           
float coefficients[FILTER_ORDER];      
float buffer[FILTER_ORDER];            
int bufferIndex = 0;                   

unsigned long lastSampleTime = 0;
const unsigned long sampleInterval = 10; 

void setup() {
  Serial.begin(115200);
  
  Serial.println("Señal_Original,Señal_Filtrada");
}

void loop() {
  if (millis() - lastSampleTime >= sampleInterval) {
    lastSampleTime = millis();

    int rawValue = analogRead(A0);
    float x_n = (float)rawValue;

    buffer[bufferIndex] = x_n;

    float y_n = 0;
    for (int k = 0; k < FILTER_ORDER; k++) {
      int index = (bufferIndex - k + FILTER_ORDER) % FILTER_ORDER;
      y_n += coefficients[k] * buffer[index];
    }
    bufferIndex = (bufferIndex + 1) % FILTER_ORDER;

    Serial.print(x_n);
    Serial.print(",");
    Serial.println(y_n);
  }
}