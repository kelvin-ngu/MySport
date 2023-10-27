import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';

import { RouterModule } from '@angular/router';
import { CommunityComponent } from './community/community.component';
import { CircleMenuComponent } from './circle-menu/circle-menu.component';
import { Component1Component } from './component1/component1.component';
import { Component2Component } from './component2/component2.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    CommunityComponent,
    CircleMenuComponent,
    Component1Component,
    Component2Component,
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot([
      {path: '', component: HomeComponent},
      {path: 'mycommunity', component: CommunityComponent}
    ]),
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
