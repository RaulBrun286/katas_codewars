object Kata {
  def smallEnough(lista: Seq[Int], numero: Int): Boolean = {
    for (almacenamiento <- lista) {
    if (almacenamiento > numero) {
      return false // Rompe la función inmediatamente si encuentra uno mayor o igual
    }
  }
  true // Si el bucle terminó y ninguno falló, entonces es true
}
}