export interface Hero {
  id: number;
  name: string;
  role: 'damage' | 'support' | 'tank';
  winRate: number;
}
