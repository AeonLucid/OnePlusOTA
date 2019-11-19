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

## Example response

```json
{
    "type": "1",
    "wipe": "0",
    "new_version": "OnePlus7TProOxygen_14.E.08_GLO_008_1911061839",
    "version_name": "OnePlus7TProOxygen_14_1911061839",
    "description": "http://otafsg.h2os.com/html/amazone2/GLO/OnePlus7TProOxygen/OnePlus7TProOxygen_14.E.08_GLO_008_1911061839/EN_0a1c2a32198123_5_0.html",
    "extract": "#OnePlus 7T Pro Oxygen OS 10.0.4.HD01BA\n\\\n##System\n\\\n\u2022 Optimized standby power consumption\n\\\n\u2022 Optimized the expanded screenshot feature\n\\\n\u2022 Optimized the Bluetooth connectivity in automobiles\n\\\n\u2022 Fixed the black bar issue while charging or playing a video\n\\\n\u2022 Updated Android security patch to 2019.10\n\\\n\u2022 Improved system stability and general bug fixes",
    "patch_name": "OnePlus7TProOxygen_14.E.08_OTA_008_all_1911061839_d196e40d.zip",
    "patch_md5": "8155a9e2a740581eca686c49b16b1d4e",
    "patch_size": "2769436441",
    "down_url": "http://otafsg.h2os.com/patch/amazone2/GLO/OnePlus7TProOxygen/OnePlus7TProOxygen_14.E.08_GLO_008_1911061839/OnePlus7TProOxygen_14.E.08_OTA_008_all_1911061839_d196e40d.zip",
    "active_url": "http://otafsg1.h2os.com/patch/amazone2/GLO/OnePlus7TProOxygen/OnePlus7TProOxygen_14.E.08_GLO_008_1911061839/OnePlus7TProOxygen_14.E.08_OTA_008_all_1911061839_d196e40d.zip",
    "recommend": "100",
    "needDataSpace": 0,
    "share": "",
    "patchFilePath": "/patch/amazone2/GLO/OnePlus7TProOxygen/OnePlus7TProOxygen_14.E.08_GLO_008_1911061839/OnePlus7TProOxygen_14.E.08_OTA_008_all_1911061839_d196e40d.zip",
    "silenceUpdate": 0,
    "noticeType": 0,
    "paramFlag": 1,
    "googlePatchLevel": 0,
    "patchId": 10197,
    "templates": [
        "5_0",
        "6_0"
    ],
    "operator": "UNKNOWN",
    "msg": "SUCCEED",
    "resultCode": 1
}
```