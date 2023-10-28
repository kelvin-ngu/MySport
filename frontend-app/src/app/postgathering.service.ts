import { Injectable, inject } from '@angular/core';
import { PostDetail } from './postdetail';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class PostgatheringService {
  postDetail!: PostDetail;
  httpClient: HttpClient  = inject(HttpClient);
  url = 'http://localhost:8000/forum/post/73d08ed3-47a0-40da-ad27-de7f41386dd7/';
  constructor() {
  }
  getPost() {
    return this.httpClient.get(this.url);
  }
}
