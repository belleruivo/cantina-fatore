// JSX - JavaScript XML -> HTML
import { useEffect, useState } from 'react'

import { useQuery } from '@tanstack/react-query'

export function App() {
  const { data } = useQuery({
    queryKey: ['summary'],
    staleTime: 1000 * 60, //60 segundos
  })

}