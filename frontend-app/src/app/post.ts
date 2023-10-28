import { Player } from "./player";

export interface Post {
    author: Player;
    category: string;
    created_at: Date;
    description: string;
    id: string;
    title: string;
    
}
