# Bug recording 
## Fuzz testing bug list
[EGALE](https://github.com/lin-tan/eagle/tree/main/bug-reproduction)

[DocTer](https://docs.google.com/spreadsheets/d/1DgupQBMVpybHtyOhCO0fRb-oJDZbZSbo7H-AG36AE_c/edit?pli=1#gid=1383411354)

[FreeFuzz](https://github.com/ise-uiuc/FreeFuzz/tree/main/data)

##  Meta's bug list and its new bugs fixed/confirmed situation
### Meta's bug list
‘*’ presents error type detected by Meta only.
<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax"> Library   </th>
    <th class="tg-0lax">Operator   </th>
    <th class="tg-0lax">Error Type   </th>
    <th class="tg-0lax"> Deivce   </th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax" rowspan="6">Tensorflow1.13.1   </td>
    <td class="tg-0lax" rowspan="3">BatchNormalize   </td>
    <td class="tg-0lax">IE-UME   </td>
    <td class="tg-0lax">GPU   </td>
  </tr>
  <tr>
    <td class="tg-0lax">IV-UME   </td>
    <td class="tg-0lax">GPU/CPU   </td>
  </tr>
  <tr>
    <td class="tg-0lax">PE*   </td>
    <td class="tg-0lax">GPU/CPU   </td>
  </tr>
  <tr>
    <td class="tg-0lax">Convlution/BatchNormalize   </td>
    <td class="tg-0lax">IE   </td>
    <td class="tg-0lax">CPU</td>
  </tr>
  <tr>
    <td class="tg-0lax">Tanh   </td>
    <td class="tg-0lax">PE* </td>
    <td class="tg-0lax">CPU   </td>
  </tr>
  <tr>
    <td class="tg-0lax">MaxPool   </td>
    <td class="tg-0lax">IE-UME   </td>
    <td class="tg-0lax">CPU   </td>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="3">Tensorflow2.3.0   </td>
    <td class="tg-0lax">BatchNormalize   </td>
    <td class="tg-0lax">IE-IVE   </td>
    <td class="tg-0lax">GPU/CPU   </td>
  </tr>
  <tr>
    <td class="tg-0lax">Convlution/BatchNormalize   </td>
    <td class="tg-0lax">IE-UME   </td>
    <td class="tg-0lax">CPU   </td>
  </tr>
  <tr>
    <td class="tg-0lax">MaxPool   </td>
    <td class="tg-0lax">IE-UME   </td>
    <td class="tg-0lax">GPU/CPU   </td>
  </tr>
  <tr>
    <td class="tg-0lax">Pytorch1.1.0   </td>
    <td class="tg-0lax">Convlution   </td>
    <td class="tg-0lax">PE*   </td>
    <td class="tg-0lax">GPU/CPU   </td>
  </tr>
  <tr>
    <td class="tg-0lax">Pytorch1.10.0   </td>
    <td class="tg-0lax">Convlution   </td>
    <td class="tg-0lax">PE*   </td>
    <td class="tg-0lax">GPU/CPU   </td>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="3">Mindspore1.0.1   <br></td>
    <td class="tg-0lax">MaxPool   </td>
    <td class="tg-0lax">IE-UME</td>
    <td class="tg-0lax">CPU</td>
  </tr>
  <tr>
    <td class="tg-0lax">Sigmoid</td>
    <td class="tg-0lax">IE-UME </td>
    <td class="tg-0lax">CPU</td>
  </tr>
  <tr>
    <td class="tg-0lax">LeakyReLU   </td>
    <td class="tg-0lax">IE-UME   </td>
    <td class="tg-0lax">CPU   </td>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="3">Mindspore1.6.1   </td>
    <td class="tg-0lax">Convlution/BatchNormalize   </td>
    <td class="tg-0lax">IE-UME   </td>
    <td class="tg-0lax">CPU   </td>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="2">MaxPool   </td>
    <td class="tg-0lax">IE-UME   </td>
    <td class="tg-0lax">CPU   </td>
  </tr>
  <tr>
    <td class="tg-0lax">PE*   </td>
    <td class="tg-0lax">GPU/CPU   </td>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="2">Mindspore1.9.0   </td>
    <td class="tg-0lax">Convlution/BatchNormalize   </td>
    <td class="tg-0lax">IE-UME   </td>
    <td class="tg-0lax">CPU   </td>
  </tr>
  <tr>
    <td class="tg-0lax">MaxPool   </td>
    <td class="tg-0lax">IE-UME   </td>
    <td class="tg-0lax">CPU   </td>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="5">MXnet1.9.1   </td>
    <td class="tg-0lax" rowspan="2">Conv   </td>
    <td class="tg-0lax"> IE-UME</td>
    <td class="tg-0lax"> CPU   </td>
  </tr>
  <tr>
    <td class="tg-0lax"> PE*   </td>
    <td class="tg-0lax">  CPU   </td>
  </tr>
  <tr>
    <td class="tg-0lax">MaxPool   </td>
    <td class="tg-0lax">IE-UME   </td>
    <td class="tg-0lax">GPU   </td>
  </tr>
  <tr>
    <td class="tg-0lax">Sigmoid   </td>
    <td class="tg-0lax">IE-UME   </td>
    <td class="tg-0lax">GPU   </td>
  </tr>
  <tr>
    <td class="tg-0lax">LeakyReLU   </td>
    <td class="tg-0lax">IE-UME   </td>
    <td class="tg-0lax">GPU   </td>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="6">MNN2.3.0   </td>
    <td class="tg-0lax"> BatchNormalize   </td>
    <td class="tg-0lax">IE-UME   </td>
    <td class="tg-0lax">GPU/CPU   </td>
  </tr>
  <tr>
    <td class="tg-0lax">Convlution   </td>
    <td class="tg-0lax">PE*   </td>
    <td class="tg-0lax">CPU</td>
  </tr>
  <tr>
    <td class="tg-0lax">Tanh </td>
    <td class="tg-0lax">PE*   </td>
    <td class="tg-0lax">CPU   </td>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="2">DeepwiseConvlution</td>
    <td class="tg-0lax">IE-UME   </td>
    <td class="tg-0lax">GPU/CPU   </td>
  </tr>
  <tr>
    <td class="tg-0lax">PE*</td>
    <td class="tg-0lax">GPU/CPU   </td>
  </tr>
  <tr>
    <td class="tg-0lax">Sigmoid   </td>
    <td class="tg-0lax">IE-UME   </td>
    <td class="tg-0lax">GPU/CPU   </td>
  </tr>
</tbody>
</table>

### Meta's new bugs fixed/confirmed situation
'Y' stands for 'YES', 'N' stands for 'NO', '-' stands for have been fixed.
<table class="tg" style="undefined;table-layout: fixed; width: 1290px">
<colgroup>
<col style="width: 192px">
<col style="width: 125px">
<col style="width: 72px">
<col style="width: 502px">
<col style="width: 57px">
<col style="width: 342px">
</colgroup>
<thead>
  <tr>
    <th class="tg-9wq8">DL&nbsp;&nbsp;&nbsp;libray</th>
    <th class="tg-9wq8">operator</th>
    <th class="tg-9wq8">Error Type</th>
    <th class="tg-9wq8">triggering condition</th>
    <th class="tg-nrix">fixed</th>
    <th class="tg-nrix">confrmed</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-9wq8" rowspan="2">Tensorflow2.15.0</td>
    <td class="tg-9wq8">BatchNormalize</td>
    <td class="tg-g0ou">IE-IVE</td>
    <td class="tg-g0ou">set epsilon&lt;0.</td>
    <td class="tg-nrix">Y</td>
    <td class="tg-nrix">-</td>
  </tr>
  <tr>
    <td class="tg-9wq8">BatchNormalize</td>
    <td class="tg-g0ou">PE</td>
    <td class="tg-g0ou">Indicating precision error</td>
    <td class="tg-nrix">Y</td>
    <td class="tg-nrix">-</td>
  </tr>
  <tr>
    <td class="tg-9wq8">Pytorch2.1.1</td>
    <td class="tg-9wq8">Convlution</td>
    <td class="tg-g0ou">PE</td>
    <td class="tg-g0ou">Indicating precision error.</td>
    <td class="tg-nrix">N</td>
    <td class="tg-nrix">N</td>
  </tr>
  <tr>
    <td class="tg-9wq8" rowspan="2">mindspore-gpu1.10.0</td>
    <td class="tg-9wq8" rowspan="2">MaxPool</td>
    <td class="tg-9wq8">IE-UME</td>
    <td class="tg-9wq8">Triggering condition is set&nbsp;&nbsp;&nbsp;device to CPU, set dataformat to NHWC.</td>
    <td class="tg-nrix">Y</td>
    <td class="tg-nrix">-</td>
  </tr>
  <tr>
    <td class="tg-nrix">PE</td>
    <td class="tg-nrix">Indicating precision error.</td>
    <td class="tg-nrix">Y</td>
    <td class="tg-nrix">-</td>
  </tr>
  <tr>
    <td class="tg-nrix" rowspan="5">MNN2.8.0</td>
    <td class="tg-nrix">BatchNormalize</td>
    <td class="tg-nrix">IE-UME</td>
    <td class="tg-nrix">Triggering condition is set epsilon and momentum.</td>
    <td class="tg-nrix">Y</td>
    <td class="tg-nrix">-</td>
  </tr>
  <tr>
    <td class="tg-nrix">Convlution</td>
    <td class="tg-nrix">PE</td>
    <td class="tg-nrix">Indicating precision error.</td>
    <td class="tg-nrix">N</td>
    <td class="tg-i2ln"><a href="https://github.com/alibaba/MNN/issues/2205">https://github.com/alibaba/MNN/issues/2205</a></td>
  </tr>
  <tr>
    <td class="tg-nrix">Tanh</td>
    <td class="tg-nrix">PE</td>
    <td class="tg-nrix">Indicating precision error</td>
    <td class="tg-nrix">N</td>
    <td class="tg-nrix">N</td>
  </tr>
  <tr>
    <td class="tg-nrix">Tanh</td>
    <td class="tg-nrix">PE</td>
    <td class="tg-nrix">Indicating precision error</td>
    <td class="tg-nrix">N</td>
    <td class="tg-i2ln"><a href="https://github.com/alibaba/MNN/issues/2241">https://github.com/alibaba/MNN/issues/2241</a></td>
  </tr>
  <tr>
    <td class="tg-nrix">DepthwiseConvlution</td>
    <td class="tg-nrix">PE</td>
    <td class="tg-nrix">Indicating precision error</td>
    <td class="tg-nrix">Y</td>
    <td class="tg-nrix">-</td>
  </tr>
</tbody>
</table>

### Meta's confirmed old bugs fixed situation
'Y' stands for 'YES', 'N' stands for 'NO'.
<table class="tg" style="undefined;table-layout: fixed; width: 850px">
<colgroup>
<col style="width: 183px">
<col style="width: 119px">
<col style="width: 69px">
<col style="width: 479px">
</colgroup>
<thead>
  <tr>
    <th class="tg-9wq8">DL&nbsp;&nbsp;&nbsp;library</th>
    <th class="tg-9wq8">Operator</th>
    <th class="tg-9wq8">fixed</th>
    <th class="tg-nrix">comfirm Link</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-9wq8" rowspan="2">Tensorflow1.13.1</td>
    <td class="tg-9wq8">Batchnormalize</td>
    <td class="tg-g0ou">Y</td>
    <td class="tg-i2ln"><a href="https://github.com/tensorflow/tensorflow/issues/59309">https://github.com/tensorflow/tensorflow/issues/59309</a></td>
  </tr>
  <tr>
    <td class="tg-9wq8">Batchnormalize</td>
    <td class="tg-g0ou">Y</td>
    <td class="tg-i2ln"><a href="https://github.com/tensorflow/tensorflow/issues/59307">https://github.com/tensorflow/tensorflow/issues/59307</a></td>
  </tr>
  <tr>
    <td class="tg-9wq8" rowspan="2">MNN2.3.0</td>
    <td class="tg-9wq8">Convlution</td>
    <td class="tg-g0ou">N</td>
    <td class="tg-i2ln"><a href="https://github.com/tensorflow/tensorflow/issues/59309">https://github.com/tensorflow/tensorflow/issues/59309</a></td>
  </tr>
  <tr>
    <td class="tg-9wq8">Tanh</td>
    <td class="tg-9wq8">N</td>
    <td class="tg-nrix">https://github.com/alibaba/MNN/issues/2241</td>
  </tr>
</tbody>
</table>
