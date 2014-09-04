snow_melt
=========


Thanks!  Here are my notes.

MODIS data in real time. 500-m resolution for things like snow, daily coverage
	* MODO-9 surface reflectance
	* Fraction snow cover, RMS error 10-12% versus landsat.
	* Time-space filtering solves for interruptions, noise
	* Pixels are different sizes.
Energy Balance Reconstruction
	* Day of full melt--> day of snow depth for most recent peak
	* Peak snow depth is a good predictor of stream runoff
	* Estimate incoming energy from solar radiation etc. Topographic downscaling
	* Also air temp, outgoing radiation
	* Based on this and day of melt, can estimate how much water was released
	* Considered pretty good, but don't know its value until 
Real time passive microwave image from a different satellite
	* The stuff you download from AMSR is off by a factor of 10.
	* In addition to poor calibration, it has low R^2. Sometimes even negative
	* Principle: ice is much more transparent in microwave range than ice is
	* Microwaves come from soil (top 5 cm), but is scattered/attenuated by ice
	* Varies with soil (liquid) moisture.
	* More emissions implies less snow.  Their algorithm uses two frequencies
	* Also, pixel size is pretty big & intensity varies a lot by day
		* Some pixels fluctuate a lot more than others
		* If snow is wet, estimates will be too low
		* If crystals are big, estimates can bee too high.
	* Microwave data is daily. Avoid the daytime data, use nighttime instead.
	* Problems: heterogeneity within pixels, vegetation, miscalibrated.
	* Estimates are too high below 100 mm and too low above.
	* Clear sensor saturation
Validation:
	* In Sierra-Nevada, we get much better estimates of how much snow actually melted
	* Reconstruction based on date of snow melt does pretty well.
	* It doesn't work until the snow has melted
	* Direct estimates of snowfall from satellites are considered unreliable


Training Data:
	MODIS snow cover % (mean and sd)
	(Other land cover?)
	topography (elevation/slope/aspect/more?)
	daily temperature, radiation
	Daily microwave data
Test data:
	Day of snow melt
