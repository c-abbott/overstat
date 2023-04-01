export interface Hero {
  key: string;
  name: string;
  portraitURL: string;
  role: 'damage' | 'support' | 'tank';
}
