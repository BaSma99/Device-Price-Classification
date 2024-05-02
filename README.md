**Dataset columns are as follows:**

■ id - ID 

■ battery_power - Total energy a battery can store in one time measured in mAh

■ blue - Has Bluetooth or not

■ clock_speed - The speed at which the microprocessor executes instructions

■ dual_sim - Has dual sim support or not

■ fc - Front Camera megapixels

■ four_g - Has 4G or not

■ int_memory - Internal Memory in Gigabytes

■ m_dep - Mobile Depth in cm

■ mobile_wt - Weight of mobile phone

■ n_cores - Number of cores of the processor

■ pc - Primary Camera megapixels

■ px_height - Pixel Resolution Height

■ px_width - Pixel Resolution Width

■ ram - Random Access Memory in Megabytes

■ sc_h - Screen Height of mobile in cm

■ sc_w - Screen Width of mobile in cm

■ talk_time - longest time that a single battery charge will last when you are

■ three_g - Has 3G or not

■ touch_screen - Has touch screen or not

■ wifi - Has wifi or not

■ price_range - This is the target variable with the value of:

● 0 (low cost)

● 1 (medium cost)

● 2 (high cost)

● 3 (very high cost)

**Modeling Steps:**

● Duild the ML model, to predict or classify the price for any device:

**Data Preparing:**
■ prepare the data very well, and do some engineering processing.

○ EDA.(Show 1-2 insights, add your comments)

■ Select and illustrate appropriate charts for the dataset to facilitate
the discovery of patterns, insights, and correlations. 

○ Train using an appropriate algorithm. 

**Evaluate the model:**

■ Show some evaluation metrics.(confusion matrix, or any other metrics, Add your comments).

**Optimize the model:**

■ Choose an appropriate algorithm to make the result good enough.(Add your comments).

**● Endpoints:**

○ RESTful API to predict the price for any device:

■ Will take the specs for any device, and send it to the ML model, then return the predicted price.

SpringBoot Project Entities:

● Device: to describe every device in our system.

EndPoints: Implement RESTful endpoints to handle the following operations

● POST /api/devices/: Retrieve a list of all devices

● GET /api/devices/{id}: Retrieve details of a specific device by ID.

● POST /api/devices: Add a new device.

● POST /api/predict/{deviceId}

○ This will call the Python API to predict the price, and save the result in the device entity here.

○ Apply some best practices here, like transaction management.

**Testing:**

● Do prediction for 10 devices from the Test dataset above.
