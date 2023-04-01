export interface Hero {
  id: string;
  name: string;
  role: 'damage' | 'support' | 'tank';
  winRate: number;
}
