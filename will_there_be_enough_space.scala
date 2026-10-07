def enough(cap: Int, on: Int, wait: Int): Int = {
  var calculo = on + wait - cap
  if calculo <= 0 then
    return 0
  else
    return calculo
    
}