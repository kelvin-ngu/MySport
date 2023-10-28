import { Component, inject, resolveForwardRef } from '@angular/core';
import { PostComponent } from '../post/post.component';
import { TabbedContentComponent } from '../tabbed-content/tabbed-content.component';
import { Router } from '@angular/router';

@Component({
  selector: 'app-community',
  templateUrl: './community.component.html',
  styleUrls: ['./community.component.css'],
  standalone: true,
  imports: [TabbedContentComponent, PostComponent]
})

export class CommunityComponent {
  constructor(private router : Router) {}

  navigateTo(route: string) {
    this.router.navigate([route]);
  }
}
