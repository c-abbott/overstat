import axios from 'axios';
import type { Hero } from './types/Hero';
import type { UserProfile } from './types/UserProfile';

const overFastApiClient = axios.create({
  baseURL: 'http://localhost:8000', // Local URL of OverFast API
});

async function getUserProfile(userId: string): Promise<UserProfile> {
  try {
    const response = await overFastApiClient.get<UserProfile>(`/user-profile/${userId}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching user profile:', error);
    throw error;
  }
}

export async function getHeroes(): Promise<Hero[]> {
  const response = await fetch(`https://overfast-api.tekrop.fr/heroes`);

  if (!response.ok) {
    throw new Error(`Error fetching heroes: ${response.statusText}`);
  }

  const heroes: Hero[] = await response.json();
  return heroes;
}

export { getUserProfile };
