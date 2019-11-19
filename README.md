# OneplusOTA

Sometimes OnePlus likes to not upload zips. 
Using this script you can fetch them the same way your phone does from the https://otag.h2os.com/post/Query_Update endpoint.

## Configuration

| Key | Description |
|-|-|
| VERSION | Property `ro.build.version.ota` |
| IMEI | [TelephonyManager#getImei(int)](https://developer.android.com/reference/android/telephony/TelephonyManager#getImei(int)) |
| PRODUCT | [Build.PRODUCT](https://developer.android.com/reference/android/os/Build.html#PRODUCT) - Use `OnePlus6T` for `OnePlus6TSingle` |
| ROM_VERSION | [Build.DISPLAY](https://developer.android.com/reference/android/os/Build.html#DISPLAY) - Replace `A6013_34` with `A6010_33` |
