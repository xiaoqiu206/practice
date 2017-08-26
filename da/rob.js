/**
算法题: 小区里别墅连着,小偷去偷,不能偷连着的2家,问怎么偷才能偷的最多
实际上就是一个数组[1, 2, 3, 4],任意不连续的元素组合,怎么组合才有最大值,最大值是多少
*/

var rob=function(nums){
  var len=nums.length;
  var result=[];
  var i;
  if(len===0){
    return 0;
  }
  if(len===1){
    return nums[0]
  }
  result[0]=nums[0];
  result[1]=Math.max(nums[1],nums[0]);
  for(i=2;i<len;i++){
    result[i]=Math.max(result[i-2]+nums[i],result[i-1]);
  }
  return result[len-1];
}

console.log(rob[1, 2, 3, 4])
console.log(rob[3, 2, 1, 5])

/**解题思路:
    用result[i]表示走到第i家时,可以偷到最大金额
    result[0]就是走到第一家的最大金额, 就是nums[0]
    result[1]就是走到第二家的最大金额,因为不可以连着偷,因此要么是nums[0], 要么是nums[1],谁大偷谁
    result[2]就是就是走到第三家的最大金额, 还是因为不能连着偷, 那么一种情况是走到第一家可以偷到的最大值(result[0])加上当前
        第三家的nums[2], 一种情况是走到第二家可以偷到的最大值(result[1])谁大取谁
    result[3]就是走到第四家的最大金额, 一种情况是走到第二家可以偷到的最大值(result[1])加上当前的nums[3], 一种情况是走到第二家
    可以偷到的最大值(result[2]), 谁大取谁

    因此, 推导出这个表达式, 走到第i家可以偷到的最大值是 走到第i-2家可以偷到的最大值(result[i-2])加上当前的nums[i],
        一种是走到第i-1家可以偷到的最大值(result[i-1]), 也就是result[i] = Math.max(result[i-2] + nums[i], result[i-1)
*/