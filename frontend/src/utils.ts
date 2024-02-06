import { jwtDecode } from 'jwt-decode'

export function isTokenExpired(token: string) {
  const { exp } = jwtDecode<{ exp: number }>(token)
  return Date.now() >= exp * 1000
}
