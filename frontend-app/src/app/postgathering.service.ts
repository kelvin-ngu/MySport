import { Injectable, inject } from '@angular/core';
import { PostDetail } from './postdetail';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class PostgatheringService {
  postDetail!: PostDetail;
  httpClient: HttpClient  = inject(HttpClient);
  url = 'http://localhost:8000/forum/post/';
  constructor() {
  }
  getPost() {
    return this.httpClient.get(this.url);
  }
}
