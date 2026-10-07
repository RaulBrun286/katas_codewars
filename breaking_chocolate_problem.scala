object Sol {

  def breakChocolate(n: Int, m: Int): Int = {
    var cortes = (n * m) - 1
    if n <= 0 || m <= 0 then
      cortes = 0
    return cortes
  }
}