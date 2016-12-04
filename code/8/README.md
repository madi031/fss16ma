# Week 8

###Datasets

<table>
<tr>
<td> Dataset </td>
<td> #Instances </td>
<td> #Attributes </td>
</tr>
<tr>
<td> <a href="https://github.com/madi031/fss16ma/tree/master/code/8/Datasets"> iris </a> </td>
<td> 150 </td>
<td> 4 </td>
</tr>
<tr>
<td> <a href="https://github.com/madi031/fss16ma/tree/master/code/8/Datasets"> credit-a </a> </td>
<td> 690 </td>
<td> 15 </td>
</tr>
<tr>
<td> <a href="https://github.com/madi031/fss16ma/tree/master/code/8/Datasets"> vote </a> </td>
<td> 435 </td>
<td> 16 </td>
</tr>
<tr>
<td> <a href="https://github.com/madi031/fss16ma/tree/master/code/8/Datasets"> sick </a> </td>
<td> 3772 </td>
<td> 30 </td>
</tr>
<tr>
<td> <a href="https://github.com/madi031/fss16ma/tree/master/code/8/Datasets"> diabetes </a> </td>
<td> 768 </td>
<td> 8 </td>
</tr>
<tr>
<td> <a href="https://github.com/madi031/fss16ma/tree/master/code/8/Datasets"> tic-tac-toe </a> </td>
<td> 958 </td>
<td> 9 </td>
</tr>
</table>

###Feature Selection using J48

<table>
<tr>
<td />
<td> #Features </td>
<td />
<td> Recall </td>
<td />
<td> Precision </td>
<td />
</tr>
<tr>
<td> Dataset </td>
<td> All </td>
<td> Selected </td>
<td> All </td>
<td> Selected </td>
<td> All </td>
<td> Selected </td>
</tr>
<tr>
<td> iris </td>
<td> 4 </td>
<td> 1 </td>
<td> 0.94 </td>
<td> 0.94 </td>
<td> 0.94 </td>
<td> 0.887 </td>
</tr>
<tr>
<td> credit-a </td>
<td> 15 </td>
<td> 3 </td>
<td> 0.88 </td>
<td> 0.802 </td>
<td> 0.871 </td>
<td> 0.925 </td>
</tr>
<tr>
<td> vote </td>
<td> 16 </td>
<td> 1 </td>
<td> 0.97 </td>
<td> 0.948 </td>
<td> 0.97 </td>
<td> 0.981 </td>
</tr>
<tr>
<td> sick </td>
<td> 29 </td>
<td> 2 </td>
<td> 0.995 </td>
<td> 0.987 </td>
<td> 0.992 </td>
<td> 0.987 </td>
</tr>
<tr>
<td> diabetes </td>
<td> 8 </td>
<td> 4 </td>
<td> 0.814 </td>
<td> 0.84 </td>
<td> 0.79 </td>
<td> 0.779 </td>
</tr>
<tr>
<td> tic-tac-toe </td>
<td> 9 </td>
<td> 2 </td>
<td> 0.887 </td>
<td> 0.885 </td>
<td> 0.878 </td>
<td> 0.707 </td>
</tr>
</table>

### Feature Selection using Wrapper

<table>
<tr>
<td />
<td> #Features </td>
<td />
<td> Recall </td>
<td />
<td> Precision </td>
<td />
</tr>
<tr>
<td> Dataset </td>
<td> All </td>
<td> Selected </td>
<td> All </td>
<td> Selected </td>
<td> All </td>
<td> Selected </td>
</tr>
<tr>
<td> iris </td>
<td> 4 </td>
<td> 1 </td>
<td> 0.94 </td>
<td> 0.96 </td>
<td> 0.94 </td>
<td> 0.889 </td>
</tr>
<tr>
<td> credit-a </td>
<td> 15 </td>
<td> 2 </td>
<td> 0.88 </td>
<td> 0.802 </td>
<td> 0.871 </td>
<td> 0.911 </td>
</tr>
<tr>
<td> vote </td>
<td> 16 </td>
<td> 1 </td>
<td> 0.97 </td>
<td> 0.948 </td>
<td> 0.97 </td>
<td> 0.981 </td>
</tr>
<tr>
<td> sick </td>
<td> 29 </td>
<td> 9 </td>
<td> 0.995 </td>
<td> 0.995 </td>
<td> 0.992 </td>
<td> 0.993 </td>
</tr>
<tr>
<td> diabetes </td>
<td> 8 </td>
<td> 4 </td>
<td> 0.814 </td>
<td> 0.842 </td>
<td> 0.79 </td>
<td> 0.797 </td>
</tr>
<tr>
<td> tic-tac-toe </td>
<td> 9 </td>
<td> 9 </td>
<td> 0.887 </td>
<td> 0.887 </td>
<td> 0.878 </td>
<td> 0.878 </td>
</tr>
</table>

###Feature Selection using CFS

<table>
<tr>
<td />
<td> #Features </td>
<td />
<td> Recall </td>
<td />
<td> Precision </td>
<td />
</tr>
<tr>
<td> Dataset </td>
<td> All </td>
<td> Selected </td>
<td> All </td>
<td> Selected </td>
<td> All </td>
<td> Selected </td>
</tr>
<tr>
<td> iris </td>
<td> 4 </td>
<td> 2 </td>
<td> 0.94 </td>
<td> 0.94 </td>
<td> 0.94 </td>
<td> 0.889 </td>
</tr>
<tr>
<td> credit-a </td>
<td> 15 </td>
<td> 7 </td>
<td> 0.88 </td>
<td> 0.877 </td>
<td> 0.871 </td>
<td> 0.857 </td>
</tr>
<tr>
<td> vote </td>
<td> 16 </td>
<td> 5 </td>
<td> 0.97 </td>
<td> 0.963 </td>
<td> 0.97 </td>
<td> 0.963 </td>
</tr>
<tr>
<td> sick </td>
<td> 29 </td>
<td> 6 </td>
<td> 0.995 </td>
<td> 0.987 </td>
<td> 0.992 </td>
<td> 0.986 </td>
</tr>
<tr>
<td> diabetes </td>
<td> 8 </td>
<td> 4 </td>
<td> 0.814 </td>
<td> 0.852 </td>
<td> 0.79 </td>
<td> 0.782 </td>
</tr>
<tr>
<td> tic-tac-toe </td>
<td> 9 </td>
<td> 5 </td>
<td> 0.887 </td>
<td> 0.917 </td>
<td> 0.878 </td>
<td> 0.798 </td>
</tr>
</table>
