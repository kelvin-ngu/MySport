import { Component, inject, resolveForwardRef } from '@angular/core';
import { PostComponent } from '../post/post.component';
import { TabbedContentComponent } from '../tabbed-content/tabbed-content.component';

@Component({
  selector: 'app-community',
  templateUrl: './community.component.html',
  styleUrls: ['./community.component.css'],
  standalone: true,
  imports: [TabbedContentComponent, PostComponent]
})

export class CommunityComponent {

  constructor(){

  }
}
