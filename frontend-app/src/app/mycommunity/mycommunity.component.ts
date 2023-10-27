import { Component } from '@angular/core';
import { PostComponent } from '../post/post.component';
import { PostDetail } from '../postdetail';

@Component({
  selector: 'app-mycommunity',
  templateUrl: './mycommunity.component.html',
  styleUrls: ['./mycommunity.component.css'],
  standalone: true,
  imports: [PostComponent]
})
export class MycommunityComponent {
  // postDetailList: PostDetail[] = [
  //   {
  //     id: 0,
  //     name: "Bua",
  //     content: "I don't know what I am doing",
  //     likeCount: 5
  //   },
  //   {
  //     id: 1,
  //     name: "Haz",
  //     content: "I don't know what I am doing",
  //     likeCount: 5
  //   }
  // ];
  postDetail: PostDetail = {
    id: 1,
    name: "Haz",
    content: "I don't know what I am doing",
    likeCount: 5
  }
}
