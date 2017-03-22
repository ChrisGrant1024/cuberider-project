from sagan *
import time

timeInterval = 4;
readings = 15

firstGyroDataX = 0;
firstGyroDataY = 0;
firstGyroDataZ = 0;

prevGyroDataX = 0;
prevGyroDataX = 0;
prevGyroDataY = 0;

lastGyroDataX = 0;
lastGyroDataY = 0;
lastGyroDataZ = 0;

avgGyroDataX = 0;
avgGyroDataY = 0;
avgGyroDataZ = 0;

medGyroDataX = 0;
medGyroDataY = 0;
medGyroDataZ = 0;

lowGyroDataX = 0;
lowGyroDataY = 0;
lowGyroDataZ = 0;

highGyroDataX = 0;
highGyroDataY = 0;
highGyroDataZ = 0;

print(gyroscope.measure())
print(gyroscope.x)
print(gyroscope.y)
print(gyroscope.z)

def getGyroscopeData():
	gyroData = [0, 0, 0]

	gyroData[0] = gyroscope.x
	gyroData[1] = gyroscope.y
	gyroData[2] = gyroscope.z

	return gyroData

file.open()
i = 0
while i < readings:
	gyroscopeData = getGyroscopeData()
	
	file.write("Reading " + str(i + 1) + ":")
	file.write("Time of Reading: " + time.asctime( time.localtime(time.time()) ))

	file.write("Gyroscope X:" + str(gyroscopeData[0]) + "\n")
	file.write("Gyroscope Y:" + str(gyroscopeData[1]) + "\n")
	file.write("Gyroscope Z:" + str(gyroscopeData[2]) + "\n \n")

	file.write("Difference from previous reading: \n")

	if prevGyroDataX == 0 && prevGyroDataY == 0 && prevGyroDataZ == 0:
		prevGyroDataX = gyroscopeData[0]
		prevGyroDataY = gyroscopeData[1]
		prevGyroDataZ = gyroscopeData[2]
	else:
		if prevGyroDataX > gyroscopeData[0]:
			file.write("Difference X: " + str(prevGyroDataX - gyroscopeData[0]))
		else:
			file.write("Difference X: " + str(gyroscopeData[0] - prevGyroDataX))

		if prevGyroDataY > gyroscopeData[1]:
			file.write("Difference Y: " + str(prevGyroDataY - gyroscopeData[1]))
		else:
			file.write("Difference Y: " + str(gyroscopeData[1] - prevGyroDataY))

		if prevGyroDataZ > gyroscopeData[2]:
			file.write("Difference Z: " + str(prevGyroDataZ - gyroscopeData[2]))
		else:
			file.write("Difference Z: " + str(gyroscopeData[2] - prevGyroDataZ))

	if avgGyroDataX == 0 && avgGyroDataY == 0 && avgGyroDataZ == 0:
		avgGyroDataX = str(gyroscopeData[0])
		avgGyroDataY = str(gyroscopeData[1])
		avgGyroDataZ = str(gyroscopeData[2])
	else:
		avgGyroDataX = (avgGyroDataX + gyroscopeData[0]) / 2
		avgGyroDataY = (avgGyroDataY + gyroscopeData[1]) / 2
		avgGyroDataZ = (avgGyroDataZ + gyroscopeData[2]) / 2

	if lowGyroDataX == 0 && lowGyroDataY == 0 && lowGyroDataZ == 0:
		lowGyroDataX = gyroscopeData[0]
		lowGyroDataY = gyroscopeData[1]
		lowGyroDataZ = gyroscopeData[2]

	if lowGyroDataX > gyroscopeData[0]:
		lowGyroDataX = gyroscopeData[0]

	if lowGyroDataY > gyroscopeData[1]:
		lowGyroDataY = gyroscopeData[1]

	if lowGyroDataZ > gyroscopeData[2]:
		lowGyroDataZ = gyroscopeData[2]

	if highGyroDataX == 0 && highGyroDataY == 0 && highGyroDataZ == 0:
		highGyroDataX = gyroscopeData[0]
		highGyroDataY = gyroscopeData[1]
		highGyroDataZ = gyroscopeData[2]

	if highGyroDataX > gyroscopeData[0]:
		highGyroDataX = gyroscopeData[0]

	if highGyroDataY > gyroscopeData[1]:
		highGyroDataY = gyroscopeData[1]

	if highGyroDataZ > gyroscopeData[2]:
		highGyroDataZ = gyroscopeData[2]

	if i == 0:
		firstGyroDataX = gyroscopeData[0]
		firstGyroDataY = gyroscopeData[1]
		firstGyroDataZ = gyroscopeData[2]
	elif i == readings:
		lastGyroDataX = gyroscopeData[0]
		lastGyroDataY = gyroscopeData[1]
		lastGyroDataZ = gyroscopeData[2]



	i += 1

	time.sleep(timeInterval)

medGyroDataX = (lowGyroDataX + highGyroDataX) / 2
medGyroDataY = (lowGyroDataY + highGyroDataY) / 2
medGyroDataZ = (lowGyroDataZ + highGyroDataZ) / 2

file.write("Some final things: \n \n")

file.write("Average Gyroscope Values: \n")
file.write("Average Gyroscope X: " + str(avgGyroDataX) + "\n")
file.write("Average Gyroscope Y: " + str(avgGyroDataY) + "\n")
file.write("Average Gyroscope Z: " + str(avgGyroDataZ) + "\n \n")

file.write("Median Gyroscope Values:  \n")
file.write("Median Gyroscope X: " + str(medGyroDataX) + "\n")
file.write("Median Gyroscope Y: " + str(medGyroDataY) + "\n")
file.write("Median Gyroscope Z: " + str(medGyroDataZ) + "\n \n")

file.write("Total Difference from the First Reading and the Last Reading: \n")
if lastGyroDataX > firstGyroDataX:
	file.write("Gyroscope X Difference: " + str(lastGyroDataX - firstGyroDataX))
else:
	file.write("Gyroscope X Difference: " + str(firstGyroDataX - lastGyroDataX))

if lastGyroDataY > firstGyroDataY:
	file.write("Gyroscope Y Difference: " + str(lastGyroDataY - firstGyroDataY))
else:
	file.write("Gyroscope Y Difference: " + str(firstGyroDataY - lastGyroDataY))

if lastGyroDataZ > firstGyroDataZ:
	file.write("Gyroscope Z Difference: " + str(lastGyroDataZ - firstGyroDataZ))
else:
	file.write("Gyroscope Z Difference: " + str(firstGyroDataZ - lastGyroDataZ))

file.close()