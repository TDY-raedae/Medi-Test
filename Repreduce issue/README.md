# Bug recording 
## Fuzz testing bug list
[EGALE](https://github.com/lin-tan/eagle/tree/main/bug-reproduction)

[DocTer](https://docs.google.com/spreadsheets/d/1DgupQBMVpybHtyOhCO0fRb-oJDZbZSbo7H-AG36AE_c/edit?pli=1#gid=1383411354)

[FreeFuzz](https://github.com/ise-uiuc/FreeFuzz/tree/main/data)

##  Meta's error list and fixed/confirmed situation
### Meta's error list
‘*’ presents error type detected by Meta only.
<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax"> DL&nbsp;libray   </th>
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

### Meta's new errors fixed/confirmed situation

<table class="MsoNormalTable" border="0" cellspacing="0" cellpadding="0" width="1103" style="width:827.4pt;border-collapse:collapse;mso-yfti-tbllook:1184;
 mso-padding-alt:0cm 5.4pt 0cm 5.4pt">
 <tbody><tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes;height:22.7pt">
  <td width="79" nowrap="" style="width:59.0pt;border-top:solid windowtext 1.0pt;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:none;
  padding:0cm 5.4pt 0cm 5.4pt;height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><b><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">Library<o:p></o:p></span></b></p>
  </td>
  <td width="75" nowrap="" style="width:56.0pt;border-top:solid windowtext 1.0pt;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:none;
  padding:0cm 5.4pt 0cm 5.4pt;height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><b><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">Operator<o:p></o:p></span></b></p>
  </td>
  <td width="47" nowrap="" style="width:35.4pt;border-top:solid windowtext 1.0pt;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:none;
  padding:0cm 5.4pt 0cm 5.4pt;height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><b><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">Type<o:p></o:p></span></b></p>
  </td>
  <td width="480" style="width:359.9pt;border-top:solid windowtext 1.0pt;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:none;
  padding:0cm 5.4pt 0cm 5.4pt;height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><b><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">Triggering Condition<o:p></o:p></span></b></p>
  </td>
  <td width="19" nowrap="" style="width:14.2pt;border-top:solid windowtext 1.0pt;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:none;
  padding:0cm 5.4pt 0cm 5.4pt;height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><b><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">F/C?<o:p></o:p></span></b></p>
  </td>
  <td width="88" nowrap="" style="width:65.7pt;border-top:solid windowtext 1.0pt;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:none;
  padding:0cm 5.4pt 0cm 5.4pt;height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><b><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">Time<o:p></o:p></span></b></p>
  </td>
  <td width="316" nowrap="" style="width:237.2pt;border-top:solid windowtext 1.0pt;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:none;
  padding:0cm 5.4pt 0cm 5.4pt;height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><b><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">Url<o:p></o:p></span></b></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:1;height:22.7pt">
  <td width="79" nowrap="" rowspan="3" style="width:59.0pt;border:none;border-bottom:
  solid black 1.0pt;mso-border-bottom-alt:solid black .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">TF 1.13.0<o:p></o:p></span></p>
  </td>
  <td width="75" nowrap="" style="width:56.0pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">BN<o:p></o:p></span></p>
  </td>
  <td width="47" nowrap="" style="width:35.4pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">IVE<o:p></o:p></span></p>
  </td>
  <td width="480" style="width:359.9pt;padding:0cm 5.4pt 0cm 5.4pt;height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><i><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:等线;color:black;mso-font-kerning:0pt">Set
  epsilon&lt;0.<o:p></o:p></span></i></p>
  </td>
  <td width="19" nowrap="" style="width:14.2pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><b><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">Y<o:p></o:p></span></b></p>
  </td>
  <td width="88" nowrap="" style="width:65.7pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">11/15/2023<o:p></o:p></span></p>
  </td>
  <td width="316" nowrap="" style="width:237.2pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">/<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:2;height:22.7pt">
  <td width="75" nowrap="" style="width:56.0pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">BN<o:p></o:p></span></p>
  </td>
  <td width="47" nowrap="" style="width:35.4pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">PE<o:p></o:p></span></p>
  </td>
  <td width="480" style="width:359.9pt;padding:0cm 5.4pt 0cm 5.4pt;height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><i><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:等线;color:black;mso-font-kerning:0pt">Indicating
  precision error.<o:p></o:p></span></i></p>
  </td>
  <td width="19" nowrap="" style="width:14.2pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><b><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">Y<o:p></o:p></span></b></p>
  </td>
  <td width="88" nowrap="" style="width:65.7pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">11/15/2023<o:p></o:p></span></p>
  </td>
  <td width="316" nowrap="" style="width:237.2pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">/<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:3;height:22.7pt">
  <td width="75" nowrap="" style="width:56.0pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">Tanh<o:p></o:p></span></p>
  </td>
  <td width="47" nowrap="" style="width:35.4pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">PE<o:p></o:p></span></p>
  </td>
  <td width="480" style="width:359.9pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><i><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:等线;color:black;mso-font-kerning:0pt">Indicating
  precision error.<o:p></o:p></span></i></p>
  </td>
  <td width="19" nowrap="" style="width:14.2pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><b><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">Y<o:p></o:p></span></b></p>
  </td>
  <td width="88" nowrap="" style="width:65.7pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">11/15/2023<o:p></o:p></span></p>
  </td>
  <td width="316" nowrap="" style="width:237.2pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">/<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:4;height:22.7pt">
  <td width="79" nowrap="" style="width:59.0pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">TF 2.3.0<o:p></o:p></span></p>
  </td>
  <td width="75" nowrap="" style="width:56.0pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">BN<o:p></o:p></span></p>
  </td>
  <td width="47" nowrap="" style="width:35.4pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">IVE<o:p></o:p></span></p>
  </td>
  <td width="480" style="width:359.9pt;padding:0cm 5.4pt 0cm 5.4pt;height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><i><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:等线;color:black;mso-font-kerning:0pt">Triggering condition
  is to set epsilon&lt;0.<o:p></o:p></span></i></p>
  </td>
  <td width="19" nowrap="" style="width:14.2pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><b><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">Y<o:p></o:p></span></b></p>
  </td>
  <td width="88" nowrap="" style="width:65.7pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">11/15/2023<o:p></o:p></span></p>
  </td>
  <td width="316" nowrap="" style="width:237.2pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">/<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:5;height:22.7pt">
  <td width="79" nowrap="" style="width:59.0pt;border-top:solid windowtext 1.0pt;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:none;
  mso-border-top-alt:solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">PT 1.1.0<o:p></o:p></span></p>
  </td>
  <td width="75" nowrap="" style="width:56.0pt;border-top:solid windowtext 1.0pt;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:none;
  mso-border-top-alt:solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">Conv<o:p></o:p></span></p>
  </td>
  <td width="47" nowrap="" style="width:35.4pt;border-top:solid windowtext 1.0pt;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:none;
  mso-border-top-alt:solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">PE<o:p></o:p></span></p>
  </td>
  <td width="480" style="width:359.9pt;border-top:solid windowtext 1.0pt;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:none;
  mso-border-top-alt:solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><i><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:等线;color:black;mso-font-kerning:0pt">Indicating
  precision error.<o:p></o:p></span></i></p>
  </td>
  <td width="19" nowrap="" style="width:14.2pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-bottom-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><b><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">Y<o:p></o:p></span></b></p>
  </td>
  <td width="88" nowrap="" style="width:65.7pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-bottom-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">01/31/2024<o:p></o:p></span></p>
  </td>
  <td width="316" nowrap="" style="width:237.2pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-bottom-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">/<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:6;height:22.7pt">
  <td width="79" nowrap="" style="width:59.0pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">PT 1.10.0<o:p></o:p></span></p>
  </td>
  <td width="75" nowrap="" style="width:56.0pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">Conv<o:p></o:p></span></p>
  </td>
  <td width="47" nowrap="" style="width:35.4pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">PE<o:p></o:p></span></p>
  </td>
  <td width="480" style="width:359.9pt;padding:0cm 5.4pt 0cm 5.4pt;height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><i><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:等线;color:black;mso-font-kerning:0pt">Indicating
  precision error.<o:p></o:p></span></i></p>
  </td>
  <td width="19" nowrap="" style="width:14.2pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><b><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">Y<o:p></o:p></span></b></p>
  </td>
  <td width="88" nowrap="" style="width:65.7pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-bottom-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">01/31/2024<o:p></o:p></span></p>
  </td>
  <td width="316" nowrap="" style="width:237.2pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">/<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:7;height:22.7pt">
  <td width="79" nowrap="" rowspan="2" style="width:59.0pt;border-top:solid windowtext 1.0pt;
  border-left:none;border-bottom:solid black 1.0pt;border-right:none;
  mso-border-top-alt:solid windowtext .5pt;mso-border-bottom-alt:solid black .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">MS 1.6.1<o:p></o:p></span></p>
  </td>
  <td width="75" nowrap="" rowspan="2" style="width:56.0pt;border-top:solid windowtext 1.0pt;
  border-left:none;border-bottom:solid black 1.0pt;border-right:none;
  mso-border-top-alt:solid windowtext .5pt;mso-border-bottom-alt:solid black .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">MP<o:p></o:p></span></p>
  </td>
  <td width="47" nowrap="" style="width:35.4pt;border:none;border-top:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">UME<o:p></o:p></span></p>
  </td>
  <td width="480" style="width:359.9pt;border:none;border-top:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><i><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:等线;color:black;mso-font-kerning:0pt">Triggering
  condition is set&nbsp;device to CPU, set dataformat to NHWC.<o:p></o:p></span></i></p>
  </td>
  <td width="19" nowrap="" style="width:14.2pt;border:none;border-top:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><b><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">Y<o:p></o:p></span></b></p>
  </td>
  <td width="88" nowrap="" style="width:65.7pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">10/28/2023<o:p></o:p></span></p>
  </td>
  <td width="316" nowrap="" style="width:237.2pt;border:none;border-top:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">/<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:8;height:22.7pt">
  <td width="47" nowrap="" style="width:35.4pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">PE<o:p></o:p></span></p>
  </td>
  <td width="480" style="width:359.9pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><i><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:等线;color:black;mso-font-kerning:0pt">Indicating
  precision error.<o:p></o:p></span></i></p>
  </td>
  <td width="19" nowrap="" style="width:14.2pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><b><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">Y<o:p></o:p></span></b></p>
  </td>
  <td width="88" nowrap="" style="width:65.7pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">10/28/2023<o:p></o:p></span></p>
  </td>
  <td width="316" nowrap="" style="width:237.2pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">/<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:9;height:22.7pt">
  <td width="79" nowrap="" rowspan="2" style="width:59.0pt;border:none;border-bottom:
  solid black 1.0pt;mso-border-bottom-alt:solid black .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">MX 1.9.1<o:p></o:p></span></p>
  </td>
  <td width="75" nowrap="" rowspan="2" style="width:56.0pt;border:none;border-bottom:
  solid black 1.0pt;mso-border-bottom-alt:solid black .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">Conv<o:p></o:p></span></p>
  </td>
  <td width="47" nowrap="" style="width:35.4pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">UME<o:p></o:p></span></p>
  </td>
  <td width="480" style="width:359.9pt;padding:0cm 5.4pt 0cm 5.4pt;height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><i><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:等线;color:black;mso-font-kerning:0pt">Triggering
  condition is set device to CPU, set dataformat to NHWC.<o:p></o:p></span></i></p>
  </td>
  <td width="19" nowrap="" style="width:14.2pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><b><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">Y<o:p></o:p></span></b></p>
  </td>
  <td width="88" nowrap="" style="width:65.7pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">01/26/2023<o:p></o:p></span></p>
  </td>
  <td width="316" nowrap="" style="width:237.2pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">https://github.com/apache/mxnet/issues/21176<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:10;height:22.7pt">
  <td width="47" nowrap="" style="width:35.4pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">PE<o:p></o:p></span></p>
  </td>
  <td width="480" style="width:359.9pt;padding:0cm 5.4pt 0cm 5.4pt;height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><i><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:等线;color:black;mso-font-kerning:0pt">Indicating
  precision error.<o:p></o:p></span></i></p>
  </td>
  <td width="19" nowrap="" style="width:14.2pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">N<o:p></o:p></span></p>
  </td>
  <td width="88" nowrap="" style="width:65.7pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">/<o:p></o:p></span></p>
  </td>
  <td width="316" nowrap="" style="width:237.2pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">/<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:11;height:22.7pt">
  <td width="79" nowrap="" rowspan="4" style="width:59.0pt;border:none;border-bottom:
  solid black 1.0pt;padding:0cm 5.4pt 0cm 5.4pt;height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">MNN 2.3.0<o:p></o:p></span></p>
  </td>
  <td width="75" nowrap="" style="width:56.0pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">BN<o:p></o:p></span></p>
  </td>
  <td width="47" nowrap="" style="width:35.4pt;border:none;border-top:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">UME<o:p></o:p></span></p>
  </td>
  <td width="480" style="width:359.9pt;border:none;border-top:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><i><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:等线;color:black;mso-font-kerning:0pt">Triggering
  condition is set epsilon and momentum.<o:p></o:p></span></i></p>
  </td>
  <td width="19" nowrap="" style="width:14.2pt;border:none;border-top:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><b><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">Y<o:p></o:p></span></b></p>
  </td>
  <td width="88" nowrap="" style="width:65.7pt;border:none;border-top:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">12/29/2023<o:p></o:p></span></p>
  </td>
  <td width="316" nowrap="" style="width:237.2pt;border:none;border-top:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">/<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:12;height:22.7pt">
  <td width="75" nowrap="" style="width:56.0pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">Conv<o:p></o:p></span></p>
  </td>
  <td width="47" nowrap="" style="width:35.4pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">PE<o:p></o:p></span></p>
  </td>
  <td width="480" style="width:359.9pt;padding:0cm 5.4pt 0cm 5.4pt;height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><i><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:等线;color:black;mso-font-kerning:0pt">Indicating
  precision error.<o:p></o:p></span></i></p>
  </td>
  <td width="19" nowrap="" style="width:14.2pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><b><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">Y<o:p></o:p></span></b></p>
  </td>
  <td width="88" nowrap="" style="width:65.7pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">02/25/2023<o:p></o:p></span></p>
  </td>
  <td width="316" nowrap="" style="width:237.2pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">https://github.com/alibaba/MNN/issues/2241<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:13;height:22.7pt">
  <td width="75" nowrap="" style="width:56.0pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">Tanh<o:p></o:p></span></p>
  </td>
  <td width="47" nowrap="" style="width:35.4pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">PE<o:p></o:p></span></p>
  </td>
  <td width="480" style="width:359.9pt;padding:0cm 5.4pt 0cm 5.4pt;height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><i><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:等线;color:black;mso-font-kerning:0pt">Indicating
  precision error.<o:p></o:p></span></i></p>
  </td>
  <td width="19" nowrap="" style="width:14.2pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><b><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">Y<o:p></o:p></span></b></p>
  </td>
  <td width="88" nowrap="" style="width:65.7pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">08/14/2020<o:p></o:p></span></p>
  </td>
  <td width="316" nowrap="" style="width:237.2pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">https://github.com/alibaba/MNN/issues/1060<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:14;mso-yfti-lastrow:yes;height:22.7pt">
  <td width="75" nowrap="" style="width:56.0pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">DWConv<o:p></o:p></span></p>
  </td>
  <td width="47" nowrap="" style="width:35.4pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">PE<o:p></o:p></span></p>
  </td>
  <td width="480" style="width:359.9pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><i><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Times New Roman&quot;,serif;
  mso-fareast-font-family:等线;color:black;mso-font-kerning:0pt">Indicating
  precision error.<o:p></o:p></span></i></p>
  </td>
  <td width="19" nowrap="" style="width:14.2pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><b><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">Y<o:p></o:p></span></b></p>
  </td>
  <td width="88" nowrap="" style="width:65.7pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">12/29/2023<o:p></o:p></span></p>
  </td>
  <td width="316" nowrap="" style="width:237.2pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:22.7pt">
  <p class="MsoNormal" align="center" style="text-align:center;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;font-family:&quot;Arial Unicode MS&quot;,sans-serif;
  color:black;mso-font-kerning:0pt">/<o:p></o:p></span></p>
  </td>
 </tr>
</tbody></table>

### Meta's confirmed old errors fixed situation
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
    <th class="tg-9wq8">DL&nbsp;library</th>
    <th class="tg-9wq8">Operator</th>
    <th class="tg-9wq8">Fixed</th>
    <th class="tg-nrix">Comfirmed Link</th>
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
    <td class="tg-i2ln"><a href="https://github.com/alibaba/MNN/issues/1060">https://github.com/alibaba/MNN/issues/1060</a></td>
  </tr>
  <tr>
    <td class="tg-9wq8">Tanh</td>
    <td class="tg-9wq8">N</td>
    <td class="tg-nrix">https://github.com/alibaba/MNN/issues/2241</td>
  </tr>
</tbody>
</table>
