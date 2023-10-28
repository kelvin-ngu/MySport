import { Component, inject, resolveForwardRef } from '@angular/core';
import { PostComponent } from '../post/post.component';
import { PostDetail } from '../postdetail';
import { PostgatheringService } from '../postgathering.service';
import { Postlist } from '../postlist';
import { TabbedContentComponent } from '../tabbed-content/tabbed-content.component';

@Component({
  selector: 'app-community',
  templateUrl: './community.component.html',
  styleUrls: ['./community.component.css'],
  standalone: true,
  imports: [TabbedContentComponent, PostComponent]
})

export class CommunityComponent {
  postgatheringService: PostgatheringService  = inject(PostgatheringService);
  postList!: Postlist;
  constructor(){
    this.postgatheringService.getPost().subscribe((response) => {
      const jsonString = JSON.stringify(response);
      this.postList = JSON.parse(jsonString);
      console.log(this.postList);
    });

  }
}
